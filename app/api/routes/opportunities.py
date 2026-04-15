from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.database import get_db

router = APIRouter()


@router.get("/opportunities")
def get_opportunities(db=Depends(get_db)):

    result = db.execute(text("SELECT 1 as test"))

    return [dict(r._mapping) for r in result]