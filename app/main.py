from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.opportunities import router as opportunities_router
from app.api.routes.predictions import router as predictions_router
from app.api.routes.internal_generate_pipeline import router as pipeline_router

from app.database import engine

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

@app.on_event("startup")
def startup():
    try:
        with engine.connect() as conn:
            print("BANCO CONECTADO")
    except Exception as e:
        print("ERRO BANCO:", e)

@app.get("/")
def root():
    return {"status": "API OK"}