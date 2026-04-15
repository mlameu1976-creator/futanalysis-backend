from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

print("🔥 MATCH CERTO CARREGADO")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)

    league_id = Column(Integer, ForeignKey("leagues.id"))

    home_team = Column(String)
    away_team = Column(String)
    date = Column(DateTime)

    # 🔥 REFERÊNCIA COMPLETA
    league = relationship(
        "app.models.league.League",
        back_populates="matches"
    )

    opportunities = relationship(
        "app.models.opportunity.Opportunity",
        back_populates="match"
    )