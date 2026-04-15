from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

print("🔥 DATABASE_URL USADO:", os.getenv("DATABASE_URL"))

DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ BASE PRIMEIRO (OBRIGATÓRIO)
Base = declarative_base()

# ✅ ENGINE
engine = create_engine(DATABASE_URL)

# ✅ SESSION
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# ✅ IMPORTAÇÃO EXPLÍCITA DOS MODELS (SEM AMBIGUIDADE)
import app.models.match
import app.models.league
import app.models.opportunity


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()