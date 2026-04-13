from fastapi import APIRouter
import subprocess
import sys

router = APIRouter()


@router.get("/run-pipeline")
def run_pipeline():

    try:
        result = subprocess.run(
            [sys.executable, "-m", "app.pipeline.run_full_multi_league_pipeline"],
            capture_output=True,
            text=True
        )

        return {
            "status": "pipeline executado",
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except Exception as e:
        return {
            "status": "erro",
            "message": str(e)
        }