from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# models precisam ser importados ANTES do configure_mappers
from app.models import match, league, opportunity, team_stats, historical_match, pre_match_features, opportunity_result

from sqlalchemy.orm import configure_mappers
configure_mappers()

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.internal_generate_pipeline import router as pipeline_router

app = FastAPI(title="FutAnalysis API")

origins = [
    "http://localhost:3000",
    "https://fut-analysis.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(opportunities_router)
app.include_router(predictions_router)
app.include_router(pipeline_router)