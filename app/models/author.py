from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

import uuid
from sqlalchemy import event

Base  = declarative_base()

class Author(Base):
    __tablename__ = "author"

    id  = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)



@event.listens_for(Author, 'before_insert')
def before_insert(mapper, connect, target):
    target.id = str(uuid.uuid4())