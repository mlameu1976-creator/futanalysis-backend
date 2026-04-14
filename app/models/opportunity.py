from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Opportunity(Base):

    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)

    match_id = Column(Integer, ForeignKey("matches.id"))

    market = Column(String)
    probability = Column(Float)

    # 🔥 RELACIONAMENTO CORRETO
    match = relationship("Match", back_populates="opportunities")