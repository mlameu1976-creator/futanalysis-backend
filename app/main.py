from fastapi import FastAPI

from app.database import Base, engine

from app.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"status": "API OK"}