import email
import string
from fastapi import APIRouter, Depends, HTTPException

from fastapi_sqlalchemy import db

from app.schema.entry import RequestEntry, ResponseEntry
from app.models.entry import Entry as ModelEntry

from app.security import get_api_key
from fastapi.security.api_key import APIKey

from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix='/entry')


@router.get('/{id}', response_model=ResponseEntry, status_code=200, tags=['Entry'])
async def get_entry_by_id(id: str, api_key: APIKey = Depends(get_api_key)):
    """Get entry based in theri id

    Args:
        id (str): the entry id
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Raises:
        HTTPException: 404 - Entry not found

    Returns:
        Entry: The requested entry
    """
    entry = db.session.query(ModelEntry).filter(ModelEntry.id == id).first()

    if entry is None:
        raise HTTPException(status_code=404, detail='Entry not found')

    return entry


@router.get('/', response_model=list[ResponseEntry], status_code=200, tags=['Entry'])
async def list_entries(api_key: APIKey = Depends(get_api_key)):
    """List all entries from database

    Args:
        api_key (APIKey, optional): _description_. Defaults to Depends(get_api_key).

    Returns:
        list[Entry]: the entry list
    """
    entry = db.session.query(ModelEntry).all()
    return entry


@router.post('/', response_model=ResponseEntry, status_code=201, tags=['Entry'])
async def create_entry(entry: RequestEntry, api_key: APIKey = Depends(get_api_key)):
    """Create new Entry

    Args:
        entry (RequestEntry): The new entry json information
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Raises:
        HTTPException: 500 - cannot create entry

    Returns:
        Entry: The created entry
    """
    db_entry = ModelEntry(
        description=entry.description,
        incomme=entry.incomme,
        value=entry.value,
        author_id=entry.author_id
    )

    try:
        db.session.add(db_entry)
        db.session.commit()
    except (TypeError, IntegrityError):
        raise HTTPException(
            status_code=500,
            detail="description, incomme, value, and author_id fields should not be empty"
        )

    return db_entry


@router.put('/{id}', response_model=ResponseEntry, status_code=200, tags=['Entry'])
async def update_entry(id: str, entry: RequestEntry, api_key: APIKey = Depends(get_api_key)):
    """Update entry

    Args:
        id (str): the entry id
        entry (RequestEntry): the entry new information
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).

    Returns:
        Entry: the updated entry
    """
    db_entry = db.session.query(ModelEntry).filter(ModelEntry.id == id).first()

    db_entry.description = entry.description
    db_entry.incomme = entry.incomme
    db_entry.value = entry.value
    db_entry.author_id = entry.author_id

    db.session.add(db_entry)
    db.session.commit()

    return db_entry


@router.delete('/{id}', status_code=204, tags=['Entry'])
async def delete_entry(id: str, api_key: APIKey = Depends(get_api_key)):
    """Delete the entry based in their ID

    Args:
        id (str): the entry id
        api_key (APIKey, optional): the header API Key. Defaults to Depends(get_api_key).
    """
    db_entry = db.session.query(ModelEntry).filter(ModelEntry.id == id).first()

    db.session.delete(db_entry)
    db.session.commit()
