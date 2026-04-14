from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 🔥 FUNÇÃO QUE ESTAVA FALTANDO (CRÍTICA)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔥 IMPORTAÇÃO FORÇADA DOS MODELS (MANTER)
from app.models import match
from app.models import league
from app.models import opportunity