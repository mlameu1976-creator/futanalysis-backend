from fastapi import FastAPI

# 🔥 IMPORTAR MODELS PRIMEIRO (CRÍTICO)
import app.models.load_models

from sqlalchemy.orm import configure_mappers
configure_mappers()

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API OK"}