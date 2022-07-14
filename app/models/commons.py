from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class CommomBase(Base):
    """Commom abstract base to be extended by others tables mapping and insert the 
       ID, CREATED and UPDATED date.

    Args:
        Base (_DeclarativeBase): the sqlalchemy declarative Base
    """
    __abstract__ = True

    id  = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime(timezone=True), server_default=func.now())
    updated = Column(DateTime(timezone=True), onupdate=func.now())