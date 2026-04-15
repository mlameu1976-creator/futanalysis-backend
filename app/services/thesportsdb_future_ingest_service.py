import requests
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
import pytz

from app.models.match import Match
from app.models.league import League


API_KEY = "844189"
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"


def ingest_future_matches(db: Session, league_id: int):

    print(f"📡 Buscando jogos futuros da liga {league_id}...")

    league = db.query(League).filter(
        League.external_id == league_id
    ).first()

    if not league:
        print("⚠️ Liga não encontrada no banco")
        return 0

    url = f"{BASE_URL}/eventsnextleague.php?id={league.external_id}"

    try:
        response = requests.get(url, timeout=30)
        data = response.json()
    except Exception as e:
        print("❌ Erro API:", e)
        return 0

    events = data.get("events")

    if not events:
        print("⚠️ Nenhum evento retornado")
        return 0

    rows = []

    for event in events:

        event_id = event.get("idEvent")

        if not event_id:
            continue

        date_str = event.get("dateEvent")
        time_str = event.get("strTime") or "00:00:00"

        if not date_str:
            continue

        try:
            utc_datetime = datetime.strptime(
                f"{date_str} {time_str}",
                "%Y-%m-%d %H:%M:%S"
            )

            utc = pytz.utc
            brasil = pytz.timezone("America/Sao_Paulo")

            utc_datetime = utc.localize(utc_datetime)
            match_date = utc_datetime.astimezone(brasil)

        except Exception as e:
            print("❌ Erro ao converter data:", e)
            continue

        rows.append({
            # 🔥 IMPORTANTE: usar id direto
            "id": int(event_id),

            "league_id": league.id,
            "home_team": event.get("strHomeTeam"),
            "away_team": event.get("strAwayTeam"),

            # 🔥 NOME CORRETO DO CAMPO
            "date": match_date
        })

    if not rows:
        print("⚠️ Nenhum jogo válido após processamento")
        return 0

    stmt = insert(Match).values(rows)

    # 🔥 CONFLITO PELO ID (PK)
    stmt = stmt.on_conflict_do_nothing(index_elements=["id"])

    db.execute(stmt)
    db.commit()

    print(f"✅ Jogos inseridos: {len(rows)}")

    return len(rows)