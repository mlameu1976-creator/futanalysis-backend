from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    country = Column(String)
    external_id = Column(Integer, unique=True)

    # 🔥 USAR STRING EXPLÍCITA + MODULE PATH
    matches = relationship(
        "app.models.match.Match",
        back_populates="league"
    )