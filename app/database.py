from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

print("🔥 DATABASE_URL USADO:", os.getenv("DATABASE_URL"))

DATABASE_URL = os.getenv("DATABASE_URL")

# 🔥 BASE DEVE VIR ANTES DE TUDO
Base = declarative_base()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 🔥 AGORA IMPORTA OS MODELS (ORDEM CORRETA)
from app.models.match import Match
from app.models.league import League
from app.models.opportunity import Opportunity


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()