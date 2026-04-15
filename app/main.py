from fastapi import FastAPI
from sqlalchemy.orm import configure_mappers

from app.database import engine
from app.db.base import Base

# 🔥 IMPORTAR TODOS OS MODELS AQUI (CENTRALIZADO)
import app.models.match
import app.models.league
import app.models.opportunity

app = FastAPI()


@app.on_event("startup")
def startup():
    print("🚀 Inicializando aplicação...")

    # 🔥 GARANTE QUE TODOS OS MAPPERS SEJAM RESOLVIDOS
    configure_mappers()

    # 🔥 CRIA TABELAS
    Base.metadata.create_all(bind=engine)

    print("✅ Mappers configurados e tabelas criadas")