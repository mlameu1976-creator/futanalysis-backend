from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import timedelta

from app.database import get_db
from app.models.match import Match
from app.models.opportunity import Opportunity
from app.models.league import League


router = APIRouter()


@router.get("/opportunities")
def get_opportunities(
    date: str = Query("all"),
    limit: int = Query(100),
    db: Session = Depends(get_db)
):

    try:

        query = (
            db.query(
                Opportunity.id,
                Match.home_team,
                Match.away_team,
                Match.match_date,
                League.name.label("league"),
                Opportunity.market,
                Opportunity.probability,
            )
            .join(Match, Opportunity.match_id == Match.id)

            # 🔥 JOIN SIMPLES (SEM CAST)
            .join(League, Match.league_id == League.external_id)

            .filter(func.date(Match.match_date) >= func.current_date())
        )

        if date == "today":
            query = query.filter(
                func.date(Match.match_date) == func.current_date()
            )

        elif date == "tomorrow":
            query = query.filter(
                func.date(Match.match_date) == func.current_date() + 1
            )

        results = query.order_by(Match.match_date.asc()).limit(limit).all()

        return [
            {
                "id": row.id,
                "home_team": row.home_team,
                "away_team": row.away_team,
                "match_date": row.match_date - timedelta(hours=3),
                "league": row.league,
                "market": row.market,
                "probability": row.probability,
            }
            for row in results
        ]

    except Exception as e:
        print("❌ ERRO NA ROTA OPPORTUNITIES:", e)
        return {"error": str(e)}