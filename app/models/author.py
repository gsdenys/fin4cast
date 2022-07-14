from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class Author(Base):
    __tablename__ = "author"

    id  = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


