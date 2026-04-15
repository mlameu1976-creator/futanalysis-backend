from fastapi import FastAPI
from app.database import engine
from app.db.base import Base

app = FastAPI()


@app.on_event("startup")
def startup():
    print("🚀 Startup iniciado")

    # 🔥 IMPORTA MODELS AQUI (CONTROLADO)
    import app.models.match
    import app.models.league
    import app.models.opportunity

    # 🔥 NÃO CHAMAR configure_mappers()
    # 🔥 NÃO USAR RELATIONSHIPS

    Base.metadata.create_all(bind=engine)

    print("✅ Banco pronto")