from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.car as car_schema
import api.cruds.car as car_crud
from api.db import get_db

router = APIRouter()


@router.get("/cars", response_model=list[car_schema.Car])
async def list_cars(db: AsyncSession = Depends(get_db)):
    return await car_crud.get_cars(db)

@router.get("/cars/{cid}", response_model=car_schema.CarCreateResponse)
async def read_car(cid: int, db: AsyncSession = Depends(get_db)):
    car = await car_crud.fetch_car(db, cid)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.post("/cars", response_model=car_schema.CarCreateResponse)
async def create_car(car_body: car_schema.CarCreate, db: AsyncSession = Depends(get_db)):
    return await car_crud.create_car(db, car_body)

@router.put("/cars/{cid}", response_model=car_schema.CarCreateResponse)
async def update_car(cid:int, car_body: car_schema.CarCreate, db: AsyncSession = Depends(get_db)):
    car = await car_crud.get_car(db, cid=cid)
    if car is None:
        raise HTTPException(status_code=404, detail="car not found")
    
    return await car_crud.update_car(db, car_body, original=car)

@router.get("/carmenu", response_model=dict)
async def get_car_menulist(db: AsyncSession = Depends(get_db)):
    return await car_crud.get_car_menulist(db)