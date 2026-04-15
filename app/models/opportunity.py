from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db.base import Base


class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True)

    match_id = Column(Integer, ForeignKey("matches.id"))

    market = Column(String)
    probability = Column(Float)
    odds = Column(Float)
    ev = Column(Float)