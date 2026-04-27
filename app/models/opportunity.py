from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base


class Opportunity(Base):

    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.id"), nullable=False)
    market = Column(String, nullable=False)
    probability = Column(Float, nullable=False)
    score = Column(Float, nullable=True)