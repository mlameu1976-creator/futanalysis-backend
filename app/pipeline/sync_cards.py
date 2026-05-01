import requests
from app.database import SessionLocal
from app.models.match import Match
from app.models.match_cards import MatchCards

API_URL = "SUA_API_AQUI"

def sync_cards():
    db = SessionLocal()

    matches = db.query(Match).all()

    for match in matches:
        try:
            response = requests.get(f"{API_URL}/fixtures/{match.external_id}")
            data = response.json()

            print(data)
            break

            home_cards = data["response"][0]["statistics"][0]["cards"]["yellow"]
            away_cards = data["response"][0]["statistics"][1]["cards"]["yellow"]

            record = MatchCards(
                match_id=match.id,
                home_cards=home_cards,
                away_cards=away_cards
            )

            db.add(record)
            db.commit()

        except Exception as e:
            print(f"Erro no match {match.id}: {e}")

    db.close()

if __name__ == "__main__":
    sync_cards()