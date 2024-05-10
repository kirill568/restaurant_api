from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.client import Client

from app.schemas.client.create_client_schema import Create_client_schema
from app.schemas.client.client_schema import Client_schema
from app.schemas.client.update_client_schema import Update_client_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import crud

router = APIRouter(
    prefix="/clients", 
    tags=["clients"]
)

@router.get("", response_model=Union[List[Client_schema], None])
async def get_clients(db: AsyncSession = Depends(get_db)):
    all_items: List[Client] = await crud.get_all(Client, db)
    return all_items

@router.get("/{id}", response_model=Client_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_client(id: int, db: AsyncSession = Depends(get_db)):
    item: Client = await crud.get_by_id(Client, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Client not found"})
    
    return item

@router.post("", response_model=Entity_created)
async def create_client(item: Create_client_schema, db: AsyncSession = Depends(get_db)):
    item: Client = await crud.create(Client, item, db)
    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_client(id: int, item: Update_client_schema, db: AsyncSession = Depends(get_db)):
    item: Client = await crud.update(Client, item, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Client not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_client(id: int, db: AsyncSession = Depends(get_db)):
    item: Client = await crud.get_by_id(Client, id, db)
    if item == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Client not found"})
    
    await crud.delete(Client, id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client successfully removed"})