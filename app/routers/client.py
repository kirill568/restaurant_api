from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.client import Client

from app.schemas.client.create_client_schema import Create_client_schema
from app.schemas.client.client_schema import Client_schema
from app.schemas.client.update_client_schema import Update_client_schema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.repository import ClientRepository

from app.container import Container

from app.exceptions import NotFoundError

router = APIRouter(
    prefix="/clients", 
    tags=["clients"]
)

# dependencies
# -------------
@inject
async def valid_client_id(id: int, repository: ClientRepository = Depends(Provide[Container.client_repository])):
    client: Client = await repository.get_by_id(id)
    if client == None:
        raise NotFoundError("Client not found")
    
    return client
# -------------

@router.get("", response_model=Union[List[Client_schema], None])
@inject
async def get_clients(repository: ClientRepository = Depends(Provide[Container.client_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=Client_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_client(client: Client = Depends(valid_client_id)):    
    return client

@router.post("", response_model=EntityCreated)
@inject
async def create_client(item: Create_client_schema, repository: ClientRepository = Depends(Provide[Container.client_repository])):
    item: Client = await repository.create(item)

    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_client(item: Update_client_schema, client: Client = Depends(valid_client_id), repository: ClientRepository = Depends(Provide[Container.client_repository])):
    item: Client = await repository.update(item, client.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_client(client: Client = Depends(valid_client_id), repository: ClientRepository = Depends(Provide[Container.client_repository])):    
    await repository.delete(client.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client successfully removed"})