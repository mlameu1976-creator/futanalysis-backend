import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# CARREGA .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# FALLBACK SE NÃO EXISTIR (segurança)
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./futanalysis.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()