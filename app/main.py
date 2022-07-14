import os
import uvicorn
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.api.author import router as AuthorRouter


load_dotenv('.env')

app = FastAPI(
    title=os.environ['API_TITLE'],
    description=os.environ['API_DESCRIPTION'],
    version=os.environ["API_VERSION"],
    redoc_url=None
)

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

app.include_router(AuthorRouter, prefix="/v1")

#This is just used by programmers to run it localy
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)