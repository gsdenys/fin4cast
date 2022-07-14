from pydantic import BaseModel

class RequestAuthor(BaseModel):
    name:str

    class Config:
        orm_mode = True

class ResponseAuthor(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True