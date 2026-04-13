from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.models.match import Match
from app.models.opportunity import Opportunity


router = APIRouter()


@router.get("/opportunities")
def get_opportunities(
    limit: int = Query(100),
    db: Session = Depends(get_db)
):

    try:

        results = (
            db.query(
                Opportunity.id,
                Match.home_team,
                Match.away_team,
                Match.match_date,
                Match.league_id,  # 👈 usamos direto
                Opportunity.market,
                Opportunity.probability,
            )
            .join(Match, Opportunity.match_id == Match.id)
            .order_by(Match.match_date.asc())
            .limit(limit)
            .all()
        )

        return [
            {
                "id": row.id,
                "home_team": row.home_team,
                "away_team": row.away_team,
                "match_date": row.match_date - timedelta(hours=3),
                "league": f"League {row.league_id}",  # 👈 simples
                "market": row.market,
                "probability": row.probability,
            }
            for row in results
        ]

    except Exception as e:
        print("ERRO:", e)
        return {"error": str(e)}