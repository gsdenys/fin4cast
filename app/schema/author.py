from pydantic import BaseModel


class RequestAuthor(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class ResponseAuthor(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True

# class RequestEntry(BaseModel):
#     desc:str
#     incomme: str
#     value: float

#     class Config:
#         orm_mode = True

# class ResponseEntry(BaseModel):
#     id: str
#     desc:str
#     incomme: str
#     value: float

#     class Config:
#         orm_mode = True
