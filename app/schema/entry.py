from pydantic import BaseModel

class RequestEntry(BaseModel):
    description: str
    incomme: bool
    value: float
    author_id: str

    class Config:
        orm_mode = True


class ResponseEntry(BaseModel):
    id: str
    description: str
    incomme: bool
    value: float
    author_id: str

    class Config:
        orm_mode = True
