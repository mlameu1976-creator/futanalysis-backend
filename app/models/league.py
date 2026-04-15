from sqlalchemy import Column, Integer, String
from app.db.base import Base


class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True)

    name = Column(String)
    country = Column(String)
    external_id = Column(Integer, unique=True)