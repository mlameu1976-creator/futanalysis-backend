from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class MatchCards(Base):
    __tablename__ = "match_cards"

    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches.id"))

    home_cards = Column(Integer)
    away_cards = Column(Integer)

    match = relationship("Match")