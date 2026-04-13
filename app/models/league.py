from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class League(Base):

    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    country = Column(String)

    # 🔥 CORREÇÃO FINAL
    external_id = Column(Integer, unique=True, index=True)

    matches = relationship("Match", back_populates="league")