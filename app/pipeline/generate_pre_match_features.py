from sqlalchemy.orm import Session
from app.services.pre_match_features_service import generate_pre_match_features


def run(db):
    return generate_pre_match_features(db)


def generate_pre_match_features_pipeline(db: Session):
    return generate_pre_match_features(db)