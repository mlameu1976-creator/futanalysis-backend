import random
from sqlalchemy.orm import Session

from app.models.match import Match
from app.models.opportunity import Opportunity


def generate_opportunities(db: Session):

    print("🔥 Gerando oportunidades EV+...")

    matches = db.query(Match).all()

    created = 0

    for match in matches:

        # 🔥 PROBABILIDADE SIMULADA (depois vamos melhorar)
        probability = round(random.uniform(0.45, 0.75), 2)

        # 🔥 ODDS SIMULADAS
        odds = round(random.uniform(1.5, 2.5), 2)

        # 🔥 EV CALCULO
        ev = round((probability * odds) - 1, 3)

        # 🔥 FILTRO REAL (ESSENCIAL)
        if ev < 0.05:
            continue

        opportunity = Opportunity(
            match_id=match.id,
            market="match_winner",
            probability=probability,
            odds=odds,
            ev=ev
        )

        db.add(opportunity)
        created += 1

    db.commit()

    print(f"✅ Oportunidades criadas: {created}")