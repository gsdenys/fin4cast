import email
import string
from fastapi import APIRouter, Depends, HTTPException

from fastapi_sqlalchemy import db

from app.schema.author import RequestAuthor, ResponseAuthor
from app.models.author import Author as ModelAuthor

from app.security import get_api_key
from fastapi.security.api_key import APIKey

from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix='/author')


@router.get('/{id}', response_model=ResponseAuthor, status_code=200, tags=['Author'])
async def get_author_by_id(id: str, api_key: APIKey = Depends(get_api_key)):
    """Get an author based in their ID

    Args:
        id (str): the author ID
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Raises:
        HTTPException: 404 - author not found

    Returns:
        Author: the requested author
    """
    author = db.session.query(ModelAuthor).filter(ModelAuthor.id == id).first()

    if author is None:
        raise HTTPException(status_code=404, detail='Author not found')

    return author


@router.get('/', response_model=list[ResponseAuthor], status_code=200, tags=['Author'])
async def author(api_key: APIKey = Depends(get_api_key)):
    """List all Authors from database

    Args:
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Returns:
        List[Author]: A list of authors
    """
    author = db.session.query(ModelAuthor).all()
    return author


@router.post('/', response_model=ResponseAuthor, status_code=201, tags=['Author'])
async def create_author(author: RequestAuthor, api_key: APIKey = Depends(get_api_key)):
    """Create new Author

    Args:
        author (RequestAuthor): The author informations
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Raises:
        HTTPException: 500 - author not created

    Returns:
        Author: The created author
    """
    db_author = ModelAuthor(name=author.name, email=author.email)

    try:
        db.session.add(db_author)
        db.session.commit()
    except (TypeError, IntegrityError):
        raise HTTPException(status_code=500, detail="The email is already being used") 

    return db_author


@router.put('/{id}', response_model=ResponseAuthor, status_code=200, tags=['Author'])
async def update_author(id: str, author: RequestAuthor, api_key: APIKey = Depends(get_api_key)):
    """Updates the author

    Args:
        id (str): the author ID
        author (RequestAuthor): author's new content
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Returns:
        Author: the updated author
    """
    db_author = db.session.query(ModelAuthor).filter(ModelAuthor.id == id).first()

    db_author.name = author.name
    db_author.email = author.email

    db.session.add(db_author)
    db.session.commit()

    return db_author


@router.delete('/{id}', status_code=204, tags=['Author'])
async def delete_author(id: str, api_key: APIKey = Depends(get_api_key)):
    """Delete author based in their ID

    Args:
        id (str): the author ID
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).
    """
    db_author = db.session.query(ModelAuthor).filter(ModelAuthor.id == id).first()

    db.session.delete(db_author)
    db.session.commit()