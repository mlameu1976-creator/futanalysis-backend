from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/run-pipeline")
def run_pipeline():
    subprocess.run(["python", "app/pipeline/run_full_multi_league_pipeline.py"])
    return {"status": "pipeline executado"}