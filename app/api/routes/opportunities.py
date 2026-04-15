from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.database import get_db

router = APIRouter()


@router.get("/opportunities")
def get_opportunities(db=Depends(get_db)):

    result = db.execute(text("""
        SELECT o.*, m.home_team, m.away_team
        FROM opportunities o
        JOIN matches m ON m.id = o.match_id
        LIMIT 100
    """))

    return [dict(r) for r in result]