from sqlalchemy import Column, ForeignKey, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import event

from app.models.commons import CommomBase,  before_insert


class Entry(CommomBase):
    """The entry database mapping

    Args:
        CommomBase (CommomBase): The abstract mapping that contains some commons fields
    """
    __tablename__ = "entry"

    description = Column(String, nullable=False)
    incomme = Column(Boolean, default=False)
    value = Column(Float, nullable=False)

    author_id = Column(String, ForeignKey('author.id'))
    author = relationship('Author')


# add the event listen to be executed before data creation
event.listen(Entry, 'before_insert', before_insert)
