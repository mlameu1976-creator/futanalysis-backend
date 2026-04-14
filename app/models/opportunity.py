from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Opportunity(Base):

    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)

    match_id = Column(Integer, ForeignKey("matches.id"))

    market = Column(String)

    probability = Column(Float)

    odds = Column(Float)  # 🔥 NOVO

    ev = Column(Float)    # 🔥 NOVO

    match = relationship("Match", back_populates="opportunities")