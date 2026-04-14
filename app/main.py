from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router

app = FastAPI(title="FutAnalysis API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 ROTA PRINCIPAL (RESOLVE O 502)
@app.get("/")
def root():
    return {"status": "API ONLINE 🚀"}

# ROTAS
app.include_router(opportunities_router)
app.include_router(predictions_router)