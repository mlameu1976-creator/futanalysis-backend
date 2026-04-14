from fastapi import APIRouter
from app.pipeline.run_full_multi_league_pipeline import run_pipeline

router = APIRouter()

@router.get("/run-pipeline")
def trigger_pipeline():
    run_pipeline()
    return {"status": "pipeline executado"}