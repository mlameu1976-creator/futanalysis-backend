from fastapi import APIRouter
import subprocess

router = APIRouter()

# 🚫 NÃO RODAR AUTOMATICAMENTE
# ✅ só roda quando chamar endpoint

@router.get("/run-pipeline")
def run_pipeline():

    try:
        subprocess.Popen(
            ["python", "-m", "app.pipeline.run_full_multi_league_pipeline"],
        )

        return {"status": "pipeline iniciado"}

    except Exception as e:
        return {"error": str(e)}