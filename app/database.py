import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# pega a URL do banco do Railway
DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL DEBUG:", DATABASE_URL)

# fallback (caso rode localmente)
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:452576@localhost:5432/futanalysis"

# correção obrigatória para Railway (postgres:// → postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

# cria engine
engine = create_engine(
    DATABASE_URL,
    echo=False
)

# sessão
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# base
Base = declarative_base()

# dependency do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()