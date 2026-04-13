import requests
from sqlalchemy.orm import Session

from app.models.match import Match
from app.models.league import League


API_KEY = "844189"
BASE_URL = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}"


def ensure_league_exists(db: Session, league_id: int):

    league_id = int(league_id)

    league = db.query(League).filter(
        League.external_id == league_id
    ).first()

    if league:
        return league

    new_league = League(
        external_id=league_id,
        name=f"League {league_id}",
        country="Unknown"
    )

    db.add(new_league)
    db.commit()

    print(f"🏆 Liga criada automaticamente: {league_id}")

    return new_league


def ingest_future_matches(db: Session, league_id: int):

    league_id = int(league_id)

    ensure_league_exists(db, league_id)

    url = f"{BASE_URL}/eventsnextleague.php?id={league_id}"

    response = requests.get(url)
    data = response.json()

    if not data or not data.get("events"):
        print(f"⚠️ Sem dados para liga {league_id}")
        return

    for event in data["events"]:

        exists = db.query(Match).filter(
            Match.external_id == event["idEvent"]
        ).first()

        if exists:
            continue

        match = Match(
            external_id=event["idEvent"],
            home_team=event["strHomeTeam"],
            away_team=event["strAwayTeam"],
            match_date=event["dateEvent"] + " " + event["strTime"],
            league_id=league_id
        )

        db.add(match)

    db.commit()

    print(f"✅ Jogos inseridos para liga {league_id}")