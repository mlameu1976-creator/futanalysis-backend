from sqlalchemy.orm import Session
from app.models.match import Match
from app.models.pre_match_features import PreMatchFeatures


def generate_pre_match_features(db: Session):
    print("🔥 NOVA VERSÃO ATIVA")

    matches = db.query(Match).all()

    for match in matches:
        existing = (
            db.query(PreMatchFeatures)
            .filter(PreMatchFeatures.match_id == match.id)
            .first()
        )

        if existing:
            continue

        feature = PreMatchFeatures(
            match_id=match.id,
            avg_goals_home=0,
            avg_goals_away=0,
            form_home=0,
            form_away=0,
        )

        db.add(feature)

    db.commit()

    print("✅ FEATURES GERADAS")
