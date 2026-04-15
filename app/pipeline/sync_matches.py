import requests
from sqlalchemy import text
from datetime import datetime


API_KEY = "844189"
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"


def sync_matches(db):

    print("🚀 Inserindo jogos...")

    leagues = db.execute(text("SELECT id, external_id FROM leagues")).fetchall()

    total = 0

    for league in leagues:

        url = f"{BASE_URL}/eventsnextleague.php?id={league.external_id}"

        data = requests.get(url).json()
        events = data.get("events")

        if not events:
            continue

        for e in events:

            if not e.get("idEvent"):
                continue

            date_str = e.get("dateEvent")
            time_str = e.get("strTime") or "00:00:00"

            try:
                match_date = datetime.strptime(
                    f"{date_str} {time_str}",
                    "%Y-%m-%d %H:%M:%S"
                )
            except:
                continue

            db.execute(text("""
                INSERT INTO matches (id, league_id, home_team, away_team, date)
                VALUES (:id, :league_id, :home, :away, :date)
                ON CONFLICT (id) DO NOTHING
            """), {
                "id": int(e["idEvent"]),
                "league_id": league.id,
                "home": e.get("strHomeTeam"),
                "away": e.get("strAwayTeam"),
                "date": match_date
            })

            total += 1

    db.commit()

    print(f"✅ Jogos inseridos: {total}")