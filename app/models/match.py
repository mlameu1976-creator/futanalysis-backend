from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from app.database import Base


class Match(Base):

    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    external_id = Column(String, unique=True)
    league_id = Column(Integer, ForeignKey("leagues.id"))
    season = Column(String)
    home_team = Column(String)
    away_team = Column(String)
    match_date = Column(DateTime)
    status = Column(String)
    is_finished = Column(Boolean, default=False)
    home_goals = Column(Integer)
    away_goals = Column(Integer)
    btts = Column(Boolean)
    over_15 = Column(Boolean)
    over_25 = Column(Boolean)