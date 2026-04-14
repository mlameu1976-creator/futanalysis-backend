from fastapi import APIRouter
from app.pipeline.run_full_multi_league_pipeline import run_pipeline

router = APIRouter(prefix="", tags=["Pipeline"])


@router.get("/run-pipeline")
def execute_pipeline():
    run_pipeline()
    return {"status": "pipeline executado com sucesso"}