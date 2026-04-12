import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =========================
# PEGAR DATABASE_URL
# =========================
DATABASE_URL = os.getenv("DATABASE_URL")

# fallback local (caso não exista)
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./test.db"

# corrigir postgres://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

print("🚀 DATABASE_URL:", DATABASE_URL)

# =========================
# ENGINE SEGURO
# =========================
try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True
    )
except Exception as e:
    print("❌ ERRO AO CRIAR ENGINE:", e)
    engine = None

# =========================
# SESSION
# =========================
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
) if engine else None

Base = declarative_base()

# =========================
# DEPENDENCY
# =========================
def get_db():
    if SessionLocal is None:
        yield None
        return

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()