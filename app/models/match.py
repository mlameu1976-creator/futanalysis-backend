from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db.base import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)

    league_id = Column(Integer, ForeignKey("leagues.id"))

    home_team = Column(String)
    away_team = Column(String)
    date = Column(DateTime)