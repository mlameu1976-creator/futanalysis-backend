from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ROTAS
from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.internal_generate_pipeline import router as pipeline_router

app = FastAPI(title="FutAnalysis API")

# =========================
# CORS (APENAS UMA VEZ)
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois podemos restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# ROTAS
# =========================
app.include_router(opportunities_router)
app.include_router(predictions_router)

# rota interna para rodar pipeline manualmente
app.include_router(pipeline_router)

# =========================
# ROTA RAIZ (TESTE)
# =========================
@app.get("/")
def root():
    return {"status": "API ONLINE 🚀"}