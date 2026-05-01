from app.database import SessionLocal
from app.models.match_cards import MatchCards
from collections import defaultdict

def generate_cards_features():
    db = SessionLocal()

    data = db.query(MatchCards).all()

    team_cards = defaultdict(list)

    for row in data:
        team_cards[row.match.home_team_id].append(row.home_cards)
        team_cards[row.match.away_team_id].append(row.away_cards)

    team_avg = {}

    for team, cards in team_cards.items():
        team_avg[team] = sum(cards) / len(cards)

    print("Médias calculadas:", team_avg)

    db.close()

    return team_avg