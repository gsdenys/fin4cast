import uuid
from sqlalchemy import event

from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CommomBase(Base):
    """Commom abstract base to be extended by others tables mapping and insert the 
       ID, CREATED and UPDATED date.

    Args:
        Base (_DeclarativeBase): the sqlalchemy declarative Base
    """
    __abstract__ = True

    id = Column(String, primary_key=True, index=True)
    created = Column(DateTime(timezone=True))
    updated = Column(DateTime(timezone=True), onupdate=func.now())


def before_insert(mapper, connect, target):
    """populate the id variable with a new UUID before the register creation

    Args:
        mapper (_type_): _description_
        connect (_type_): _description_
        target (any): the target element
    """
    target.id = str(uuid.uuid4())
    target.created = func.now()
