import os
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

from starlette.status import HTTP_403_FORBIDDEN


API_KEY_NAME = "access_token"
API_KEY = "AKH6FVez6TW57BMbWWnb7X8rB856Mnme"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == API_KEY:
        return api_key_header

    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )
