from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.pipeline import router as pipeline_router



print("🔥 IMPORTANDO PIPELINE ROUTER...")

app = FastAPI(title="FutAnalysis API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROTAS
app.include_router(opportunities_router)
app.include_router(predictions_router)
app.include_router(pipeline_router)


@app.get("/")
def root():
    return {"status": "ok"}

from app.pipeline.run_full_multi_league_pipeline import run_pipeline

@app.get("/run-pipeline")
def run_pipeline_route():
    run_pipeline()
    return {"status": "pipeline executado"}