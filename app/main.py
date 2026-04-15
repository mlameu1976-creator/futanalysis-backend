from fastapi import FastAPI
from app.database import engine
from app.db.base import Base

app = FastAPI()


@app.on_event("startup")
def startup():

    # 🔥 IMPORT CONTROLADO
    from app.models.match import Match
    from app.models.league import League
    from app.models.opportunity import Opportunity

    Base.metadata.create_all(bind=engine)