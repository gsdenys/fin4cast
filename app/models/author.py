from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import event

from app.models.commons import CommomBase,  before_insert

class Author(CommomBase):
    __tablename__ = "author"

    id  = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)


event.listen(Author, 'before_insert', before_insert)

# @event.listens_for(Author, 'before_insert')
# def before_insert(mapper, connect, target):
#     target.id = str(uuid.uuid4())