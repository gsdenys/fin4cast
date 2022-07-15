from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import event

from app.models.commons import CommomBase,  before_insert


class Author(CommomBase):
    """The autor database mappin

    Args:
        CommomBase (CommomBase): The abstract mapping that contains some commons fields
    """
    __tablename__ = "author"

    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


# add the event listen to be executed before data creation
event.listen(Author, 'before_insert', before_insert)
