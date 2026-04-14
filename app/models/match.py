from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Match(Base):

    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    league_id = Column(Integer, ForeignKey("leagues.id"))

    home_team = Column(String)
    away_team = Column(String)

    date = Column(String)

    # 🔥 ADICIONAR ISSO
    external_id = Column(Integer, unique=True, index=True)
    season = Column(String)
    home_goals = Column(Integer)
    away_goals = Column(Integer)
    is_finished = Column(Boolean)

    league = relationship("League", back_populates="matches")

    # 🔥 IMPORTANTE (corrige erro anterior)
    opportunities = relationship("Opportunity", back_populates="match")