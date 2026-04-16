from fastapi import FastAPI

from app.models import base
from sqlalchemy.orm import configure_mappers

configure_mappers()

app = FastAPI()


@app.get("/")
def root():
    return {"status": "API OK"}