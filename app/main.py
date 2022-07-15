import os
import uvicorn

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app.api.author import router as AuthorRouter

# load dotenv file
from dotenv import load_dotenv
load_dotenv('.env')

# This is a modification to this code work on Heroku. When the database is created on, the unmutable
# var envirnment is inputed at the app automaticaly and this env var has the prefix 'postgres://' that
# are deprecated and already removed from the SQLAlchemy. Now the prefix is 'postgresql://'
db_env = os.environ['DATABASE_URL']
if db_env.startswith("postgres://"):
    db_env = db_env.replace("postgres://", "postgresql://")
    os.environ['DATABASE_URL'] = db_env

# create the fastapi app
app = FastAPI(
    title=os.environ['API_TITLE'],
    description=os.environ['API_DESCRIPTION'],
    version=os.environ["API_VERSION"],
    redoc_url=None
)

# add a midleware database
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# include the routers. In the nexts version, all rutes should be encapsulated in an module, so
# it'll more elegant than at the main
app.include_router(AuthorRouter, prefix="/v1")

# This is just used by programmers to run it localy
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
