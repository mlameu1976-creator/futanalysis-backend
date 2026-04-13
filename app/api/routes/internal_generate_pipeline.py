from fastapi import APIRouter
import subprocess

router = APIRouter()

@router.get("/run-pipeline")
def run_pipeline_route():

    try:
        subprocess.Popen(
            ["python", "-m", "app.pipeline.run_full_multi_league_pipeline"]
        )

        return {"status": "pipeline iniciado"}

    except Exception as e:
        return {"error": str(e)}