from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.internal_generate_pipeline import router as pipeline_router

# 🔥 IMPORTANTE
from app.database import Base, engine

app = FastAPI(title="FutAnalysis API")

# 🔥 CRIA AS TABELAS AUTOMATICAMENTE
Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rotas públicas
app.include_router(opportunities_router)
app.include_router(predictions_router)

# rotas internas (já existia)
app.include_router(pipeline_router)

# 🔥 NOVA ROTA PARA RODAR PIPELINE
@app.get("/run-pipeline")
def run_pipeline():
    from app.pipeline.run_full_multi_league_pipeline import main
    main()
    return {"status": "pipeline executado com sucesso"}
