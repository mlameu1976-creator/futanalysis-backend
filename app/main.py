from fastapi import FastAPI
from app.database import engine
from app.db.base import Base

app = FastAPI()


@app.on_event("startup")
def startup():

    print("🚀 STARTUP LIMPO")

    # IMPORT CONTROLADO
    import app.models.match
    import app.models.league
    import app.models.opportunity

    Base.metadata.create_all(bind=engine)

    print("✅ Banco pronto")


@app.get("/")
def root():
    return {"status": "ok"}