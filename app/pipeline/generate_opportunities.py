from sqlalchemy.orm import Session
from app.models.match import Match
from app.models.opportunity import Opportunity


def generate_opportunities(db: Session):

    print("🔥 Gerando oportunidades...")

    # 🔥 LIMPA ANTIGAS
    db.query(Opportunity).delete()

    matches = db.query(Match).all()

    print(f"📊 Jogos encontrados: {len(matches)}")

    count = 0

    for match in matches:

        # 🔥 DADOS MOCK (GARANTE FUNCIONAMENTO)
        probability = 0.65
        odds = 1.80

        ev = (probability * odds) - 1

        if ev > 0:
            op = Opportunity(
                match_id=match.id,
                market="over_2.5",
                probability=probability,
                odds=odds,
                ev=ev
            )

            db.add(op)
            count += 1

    db.commit()

    print(f"✅ Oportunidades geradas: {count}")