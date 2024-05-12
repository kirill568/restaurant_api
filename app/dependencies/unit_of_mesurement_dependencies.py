from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from app.models.unit_of_measurement import UnitOfMeasurement

from app.repository import UnitOfMeasurementRepository

from app.container import Container

from app.exceptions import NotFoundError

@inject
async def valid_unit_of_measurement_id(id: int, repository: UnitOfMeasurementRepository = Depends(Provide[Container.unit_of_measurement_repository])):
    unit_of_measurement: UnitOfMeasurement = await repository.get_by_id(id)
    if unit_of_measurement == None:
        raise NotFoundError("Unit of measurement not found")
    
    return unit_of_measurement