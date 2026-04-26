from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# models precisam ser importados ANTES do configure_mappers
from app.models import match, league, opportunity, team_stats, historical_match, pre_match_features, opportunity_result

from sqlalchemy.orm import configure_mappers
configure_mappers()

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.internal_generate_pipeline import router as pipeline_router

<<<<<<< HEAD
app = FastAPI(title="FutAnalysis API")

origins = [
    "http://localhost:3000",
    "https://fut-analysis.vercel.app",
]

=======
from app.database import engine

app = FastAPI(title="FutAnalysis API")

# CORS
>>>>>>> 9ddbf4c025b4624a2b344cf695f78dc35ed5126d
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

<<<<<<< HEAD
app.include_router(opportunities_router)
app.include_router(predictions_router)
app.include_router(pipeline_router)
=======
# Rotas
app.include_router(opportunities_router)
app.include_router(predictions_router)
app.include_router(pipeline_router)

# Startup
@app.on_event("startup")
def startup():
    print("🚀 STARTUP INICIADO")
    try:
        with engine.connect() as conn:
            print("✅ BANCO CONECTADO")
    except Exception as e:
        print("❌ ERRO BANCO:", e)

# Health check
@app.get("/")
def root():
    return {"status": "API OK"}
>>>>>>> 9ddbf4c025b4624a2b344cf695f78dc35ed5126d
