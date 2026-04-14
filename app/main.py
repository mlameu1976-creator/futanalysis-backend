from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔥 IMPORTA AS ROTAS
from app.api.routes.opportunities import router as opportunities_router

app = FastAPI(title="FutAnalysis API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ HEALTHCHECK (NUNCA REMOVER)
@app.get("/")
def root():
    return {"status": "API ONLINE 🚀"}

# ✅ REGISTRA ROTA
app.include_router(opportunities_router)