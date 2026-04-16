from fastapi import FastAPI

from app.models.match import Match

print("🔥 ATRIBUTOS DO MATCH:", dir(Match))
print("🔥 TEM LEAGUE?", hasattr(Match, "league"))

# 🔥 IMPORTAR MODELS PRIMEIRO (CRÍTICO)
import app.models.load_models

from sqlalchemy.orm import configure_mappers
configure_mappers()

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API OK"}