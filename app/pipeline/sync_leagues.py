import requests
from sqlalchemy.orm import Session

from app.models.league import League


API_URL = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"


TARGET_KEYWORDS = [
    "Brazil",
    "Austrian",
    "Turkey",
    "Saudi",
    "China",
    "Denmark",
    "Norway",
    "MLS",
    "Portugal",
    "Serbia",
    "Poland",
]


def sync_leagues(db: Session):

    print("Sincronizando ligas...")

    response = requests.get(API_URL, timeout=30)
    data = response.json()

    leagues = data.get("leagues", [])

    added = 0

    for league in leagues:

        name = league.get("strLeague", "")
        sport = league.get("strSport", "")
        league_id = league.get("idLeague")
        country = league.get("strCountry", "")

        if sport != "Soccer":
            continue

        allowed = False

        for keyword in TARGET_KEYWORDS:
            if keyword.lower() in name.lower() or keyword.lower() in country.lower():
                allowed = True
                break

        if not allowed:
            continue

        exists = db.query(League).filter(
            League.external_id == league_id
        ).first()

        if exists:
            continue

        new_league = League(
            name=name,
            country=country,
            external_id=league_id,
            sport="Soccer"
        )

        db.add(new_league)

        added += 1

        print(f"Liga adicionada: {name}")

    db.commit()

    print(f"Ligas adicionadas: {added}")