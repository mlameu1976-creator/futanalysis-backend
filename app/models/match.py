from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    external_id = Column(Integer, unique=True)

    home_team = Column(String)
    away_team = Column(String)

    home_goals = Column(Integer, nullable=True)
    away_goals = Column(Integer, nullable=True)

    match_date = Column(DateTime)

    season = Column(Integer)

    is_finished = Column(Boolean, default=False)

    league_id = Column(Integer, ForeignKey("leagues.id"))

    opportunities = relationship("Opportunity", back_populates="match")