from app.database import SessionLocal
from app.models.match_cards import MatchCards

db = SessionLocal()

data = db.query(MatchCards).all()

print(f"Total registros: {len(data)}")

for row in data[:5]:
    print(row.id, row.match_id, row.home_cards, row.away_cards)

db.close()