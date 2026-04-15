from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from app.db.base import Base

print("🔥 DATABASE_URL USADO:", os.getenv("DATABASE_URL"))

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔥 IMPORTS NO FINAL (SEM CIRCULAR)
import app.models.match
import app.models.league
import app.models.opportunity