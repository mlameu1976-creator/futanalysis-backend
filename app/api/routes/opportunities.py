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
    limit: int = Query(100),  # 🔥 REDUZIDO (antes 500)
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
            .outerjoin(League, Match.league_id == League.external_id)
            .filter(func.date(Match.match_date) >= func.current_date())
            .order_by(Match.match_date.asc())
            .limit(limit)
        )

        results = query.all()

        # 🔥 se não tiver dados → retorna rápido
        if not results:
            return []

        output = []

        for row in results:

            match_date = None
            if row.match_date:
                match_date = row.match_date - timedelta(hours=3)

            output.append({
                "id": row.id,
                "home_team": row.home_team or "",
                "away_team": row.away_team or "",
                "match_date": match_date,
                "league": row.league or "Unknown",
                "market": row.market or "",
                "probability": float(row.probability) if row.probability else 0,
            })

        return output

    except Exception as e:
        return {"error": str(e)}