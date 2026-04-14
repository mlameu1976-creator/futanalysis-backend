from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.internal_generate_pipeline import router as pipeline_router

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


# 🔥 CRIA AS TABELAS AUTOMATICAMENTE
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    print("🔥 TABELAS CRIADAS COM SUCESSO")