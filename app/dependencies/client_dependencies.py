from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from app.models.client import Client

from app.repository import ClientRepository

from app.container import Container

from app.exceptions import NotFoundError

@inject
async def valid_client_id(id: int, repository: ClientRepository = Depends(Provide[Container.client_repository])):
    client: Client = await repository.get_by_id(id)
    if client == None:
        raise NotFoundError("Client not found")
    
    return client