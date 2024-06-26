from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.client import Client

from app.schemas.client.create_client_schema import CreateClientSchema
from app.schemas.client.client_schema import ClientSchema
from app.schemas.client.update_client_schema import UpdateClientSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.repository import ClientRepository

from app.container import Container

from app.dependencies.client_dependencies import valid_client_id

router = APIRouter(
    prefix="/clients", 
    tags=["clients"]
)

@router.get("", response_model=Union[List[ClientSchema], None])
@inject
async def get_clients(repository: ClientRepository = Depends(Provide[Container.client_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=ClientSchema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_client(client: Client = Depends(valid_client_id)):    
    return client

@router.post("", response_model=EntityCreated)
@inject
async def create_client(item: CreateClientSchema, repository: ClientRepository = Depends(Provide[Container.client_repository])):
    item: Client = await repository.create(item)

    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_client(item: UpdateClientSchema, client: Client = Depends(valid_client_id), repository: ClientRepository = Depends(Provide[Container.client_repository])):
    item: Client = await repository.update(item, client.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_client(client: Client = Depends(valid_client_id), repository: ClientRepository = Depends(Provide[Container.client_repository])):    
    await repository.delete(client.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Client successfully removed"})