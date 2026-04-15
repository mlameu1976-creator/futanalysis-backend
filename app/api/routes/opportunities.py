from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.database import get_db

router = APIRouter()


@router.get("/opportunities")
def get_opportunities(db=Depends(get_db)):

    try:
        result = db.execute(text("""
            SELECT 
                o.id,
                o.match_id,
                o.market,
                o.probability,
                o.odds,
                o.ev,
                m.home_team,
                m.away_team
            FROM opportunities o
            LEFT JOIN matches m ON m.id = o.match_id
            LIMIT 100
        """))

        return [dict(row._mapping) for row in result]

    except Exception as e:
        return {"error_real": str(e)}