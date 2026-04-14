from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Match(Base):

    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    home_team = Column(String)
    away_team = Column(String)
    match_date = Column(DateTime)

    # 🔥 CORREÇÃO AQUI
    league_id = Column(String, ForeignKey("leagues.external_id"))

    # 🔥 RELACIONAMENTO CORRETO
    league = relationship("League", back_populates="matches")