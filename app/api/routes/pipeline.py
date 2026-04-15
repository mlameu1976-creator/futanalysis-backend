from fastapi import APIRouter, Depends
from app.database import get_db
from app.pipeline.sync_leagues import sync_leagues
from app.pipeline.sync_matches import sync_matches
from app.pipeline.generate_opportunities import generate_opportunities

router = APIRouter()

@router.get("/run-pipeline")
def run_pipeline(db=Depends(get_db)):

    print("🚀 PIPELINE MANUAL")

    sync_leagues(db)
    sync_matches(db)
    generate_opportunities(db)

    return {"status": "pipeline executado"}