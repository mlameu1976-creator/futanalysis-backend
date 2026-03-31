from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal

# ✅ IMPORT CORRETO
from app.services.pre_match_features_service import generate_pre_match_features
from app.services.opportunity_engine import run_opportunity_engine

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/internal/generate-pipeline")
def generate_pipeline(db: Session = Depends(get_db)):
    """
    Gera features + oportunidades (não quebra pipeline principal)
    """

    print("⚙️ Gerando features...")
    generate_pre_match_features(db)

    print("💰 Gerando oportunidades...")
    run_opportunity_engine(db)

    return {"status": "pipeline executado com sucesso"}