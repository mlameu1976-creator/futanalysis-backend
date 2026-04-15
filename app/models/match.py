from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    league_id = Column(Integer, ForeignKey("leagues.id"))

    home_team = Column(String)
    away_team = Column(String)
    date = Column(DateTime)

    # 🔥 ESSA LINHA É O QUE ESTÁ FALTANDO NO SEU SISTEMA
    league = relationship("League", back_populates="matches")

    # opcional (se existir Opportunity)
    opportunities = relationship("Opportunity", back_populates="match")