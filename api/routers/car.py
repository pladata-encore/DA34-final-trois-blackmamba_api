from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.car as car_schema
import api.cruds.car as car_crud
from api.db import get_db

router = APIRouter()


@router.get("/cars", response_model=list[car_schema.Car])
async def list_cars(db: AsyncSession = Depends(get_db)):
    return await car_crud.get_cars(db)


@router.post("/cars", response_model=car_schema.CarCreateResponse)
async def create_car(car_body: car_schema.CarCreate, db: AsyncSession = Depends(get_db)):
    return await car_crud.create_car(db, car_body)


@router.put("/cars/{cid}", response_model=car_schema.CarCreateResponse)
async def update_car(cid:int, car_body: car_schema.CarCreate, db: AsyncSession = Depends(get_db)):
    car = await car_crud.get_car(db, cid=cid)
    if car is None:
        raise HTTPException(status_code=404, detail="car not found")
    
    return await car_crud.update_car(db, car_body, original=car)


@router.delete("/cars/{cid}", response_model=None)
async def delete_car(cid:int, db: AsyncSession = Depends(get_db)):
    car = await car_crud.get_car(db, cid=cid)
    if car is None:
        raise HTTPException(status_code=404, detail="car not found")
    
    return await car_crud.delete_car(db, original=car)


@router.get("/cars/data", response_model=dict)
async def get_car_data(db: AsyncSession = Depends(get_db)):
    return await car_crud.get_car_data(db)


@router.get("/cars/code", response_model=str)
async def get_car_code(carCompany: str, carName: str, carYear: str, db: AsyncSession = Depends(get_db)):
    car_code = await car_crud.get_car_code(db, carCompany, carName, carYear)
    if car_code is None:
        raise HTTPException(status_code=404, detail="Car code not found")
    return car_code