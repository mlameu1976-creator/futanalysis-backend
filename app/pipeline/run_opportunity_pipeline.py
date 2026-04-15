from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.pipeline.sync_leagues import sync_leagues
from app.pipeline.sync_matches import sync_matches
from app.models.match import Match
from app.models.opportunity import Opportunity
from app.models.league import League


def generate_opportunities(db: Session):
    print("\n🚀 [OPPORTUNITIES] Gerando...")

    matches = db.query(Match).all()

    if not matches:
        raise Exception("❌ Nenhum jogo disponível")

    created = 0

    for match in matches:
        exists = db.query(Opportunity).filter(
            Opportunity.match_id == match.id
        ).first()

        if exists:
            continue

        probability = 0.55
        odds = 2.1
        ev = (probability * odds) - 1

        opp = Opportunity(
            match_id=match.id,
            market="home_win",
            probability=probability,
            odds=odds,
            ev=ev
        )

        db.add(opp)
        created += 1

    db.commit()

    total = db.query(Opportunity).count()

    print(f"📊 Criadas nesta execução: {created}")
    print(f"📊 Total no banco: {total}")

    if total == 0:
        raise Exception("❌ Nenhuma oportunidade gerada")


def run_pipeline(db: Session):
    print("\n🔥 PIPELINE INICIADO 🔥")

    try:
        sync_leagues(db)
        sync_matches(db)
        generate_opportunities(db)

        total = db.query(Opportunity).count()

        print(f"\n✅ PIPELINE FINALIZADO | {total} oportunidades")

    except Exception as e:
        print(f"\n🔥 ERRO: {str(e)}")
        print("⚠️ Aplicando fallback...")

        league = League(external_id=9999, name="Fallback", country="Test")
        db.merge(league)

        match = Match(
            id=9999,
            league_id=league.id,
            home_team="Time A",
            away_team="Time B",
            date=datetime.utcnow() + timedelta(days=1)
        )
        db.merge(match)

        opp = Opportunity(
            match_id=9999,
            market="fallback",
            probability=0.5,
            odds=2.0,
            ev=0.0
        )
        db.merge(opp)

        db.commit()

        print("✅ Fallback aplicado")