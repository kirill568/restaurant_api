from fastapi import APIRouter, status, Response, Path, Depends
from typing import Union, List
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from app.models.unit_of_measurement import Unit_of_measurement

from app.schemas.unit_of_measurement.create_unit_of_measurement_schema import Create_unit_of_measurement_schema
from app.schemas.unit_of_measurement.unit_of_measurement_schema import Unit_of_measurement_schema
from app.schemas.unit_of_measurement.update_unit_of_measurement_schema import Update_unit_of_measurement_schema

from app.schemas.responses.entity_created import Entity_created
from app.schemas.responses.message import Message

from app.repository import crud

router = APIRouter(
    prefix="/unit-of-measurement", 
    tags=["unit-of-measurement"]
)

@router.get("", response_model=Union[List[Unit_of_measurement_schema], None])
async def get_unit_of_measurements(db: AsyncSession = Depends(get_db)):
    all_items = await crud.get_all(Unit_of_measurement, db)
    return all_items

@router.get("/{id}", response_model=Unit_of_measurement_schema, responses={status.HTTP_404_NOT_FOUND: {"model": Message}})
async def get_unit_of_measurement(id: int, db: AsyncSession = Depends(get_db)):
    unit_of_measurement: Unit_of_measurement = await crud.get_by_id(Unit_of_measurement, id, db)
    if unit_of_measurement == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Unit of measurement not found"})
    
    return unit_of_measurement

@router.post("", response_model=Entity_created)
async def create_unit_of_measurement(unit_of_measurement: Create_unit_of_measurement_schema, db: AsyncSession = Depends(get_db)):
    unit_of_measurement: Unit_of_measurement = await crud.create(Unit_of_measurement, unit_of_measurement, db)
    return JSONResponse(content={"id": unit_of_measurement.id})

@router.put("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def update_product_type(id: int, unit_of_measurement: Update_unit_of_measurement_schema, db: AsyncSession = Depends(get_db)):
    unit_of_measurement: Unit_of_measurement = await crud.update(Unit_of_measurement, unit_of_measurement, id, db)
    if unit_of_measurement == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Unit of measurement not found"})

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Unit of measurement successfully updated"})

@router.delete("/{id}", responses={status.HTTP_200_OK: {"model": Message}, status.HTTP_404_NOT_FOUND: {"model": Message}})
async def remove_product_type(id: int, db: AsyncSession = Depends(get_db)):
    unit_of_measurement: Unit_of_measurement = await crud.get_by_id(Unit_of_measurement, id, db)
    if unit_of_measurement == None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Unit of measurement not found"})
    
    await crud.delete(Unit_of_measurement, id, db)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Unit of measurement successfully removed"})