from fastapi import APIRouter, status, Response, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from fastapi.responses import JSONResponse

from app.models.unit_of_measurement import UnitOfMeasurement

from app.schemas.unit_of_measurement.create_unit_of_measurement_schema import CreateUnitOfMeasurementSchema
from app.schemas.unit_of_measurement.unit_of_measurement_schema import UnitOfMeasurementSchema
from app.schemas.unit_of_measurement.update_unit_of_measurement_schema import UpdateUnitOfMeasurementSchema

from app.schemas.responses.entity_created import EntityCreated
from app.schemas.responses.message import Message

from app.repository import UnitOfMeasurementRepository

from app.container import Container

from app.dependencies.unit_of_mesurement_dependencies import valid_unit_of_measurement_id

router = APIRouter(
    prefix="/unit-of-measurement", 
    tags=["unit-of-measurement"]
)

@router.get("", response_model=Union[List[UnitOfMeasurementSchema], None])
@inject
async def get_unit_of_measurements(repository: UnitOfMeasurementRepository = Depends(Provide[Container.unit_of_measurement_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=UnitOfMeasurementSchema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def get_unit_of_measurement(unit_of_measurement: UnitOfMeasurement = Depends(valid_unit_of_measurement_id)):    
    return unit_of_measurement

@router.post("", response_model=EntityCreated)
@inject
async def create_unit_of_measurement(
    unit_of_measurement: CreateUnitOfMeasurementSchema, 
    repository: UnitOfMeasurementRepository = Depends(Provide[Container.unit_of_measurement_repository])
):
    item: UnitOfMeasurement = await repository.create(unit_of_measurement)

    return JSONResponse(content={"id": item.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def update_product_type(
    item: UpdateUnitOfMeasurementSchema, 
    unit_of_measurement: UnitOfMeasurement = Depends(valid_unit_of_measurement_id), 
    repository: UnitOfMeasurementRepository = Depends(Provide[Container.unit_of_measurement_repository])
):
    await repository.update(item, unit_of_measurement.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Unit of measurement successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
@inject
async def remove_product_type(
    unit_of_measurement: UnitOfMeasurement = Depends(valid_unit_of_measurement_id), 
    repository: UnitOfMeasurementRepository = Depends(Provide[Container.unit_of_measurement_repository])
):    
    await repository.delete(unit_of_measurement.id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Unit of measurement successfully removed"})