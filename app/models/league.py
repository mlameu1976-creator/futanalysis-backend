from sqlalchemy import Column, Integer, String

from app.database import Base


class League(Base):

    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    country = Column(String)

    external_id = Column(String, unique=True, index=True)
