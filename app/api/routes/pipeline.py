from fastapi import APIRouter

router = APIRouter()

@router.get("/run-pipeline")
def run_pipeline():
    return {"status": "DESATIVADO"}