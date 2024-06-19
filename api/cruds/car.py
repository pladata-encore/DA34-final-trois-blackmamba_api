from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.car as car_model
import api.schemas.car as car_schema

async def create_car(db: AsyncSession, car_create:car_schema.CarCreate) -> car_model.Car:
    car = car_model.Car(**car_create.dict())
    db.add(car)
    await db.commit()
    await db.refresh(car)
    return car

async def get_cars(db: AsyncSession) -> list[car_model.Car]:
    result: Result = await db.execute(
        select(
            car_model.Car
        )
    )
    return result.scalars().all()

async def get_car(db: AsyncSession, cid: int) -> car_model.Car | None:
    result: Result = await db.execute(
        select(car_model.Car).filter(car_model.Car.cid == cid)
    )
    return result.scalars().first()

async def update_car(db: AsyncSession, car_create:car_schema.CarCreate, original:car_model.Car) -> car_model.Car:
    original.carCompany = car_create.carCompany
    original.carName = car_create.carName
    original.carYear = car_create.carYear
    original.carCode = car_create.carCode
    original.isActive = car_create.isActive
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_car(db: AsyncSession, original:car_model.Car) -> None:
    await db.delete(original)
    await db.commit()

async def get_car_data(db: AsyncSession) -> dict:
    result: Result = await db.execute(
        select(
            car_model.Car.carCompany,
            car_model.Car.carName,
            car_model.Car.carYear
        )
    )
    cars = result.fetchall()
    
    car_data = {}
    for car in cars:
        carCompany, carName, carYear = car
        if carCompany not in car_data:
            car_data[carCompany] = {}
        if carName not in car_data[carCompany]:
            car_data[carCompany][carName] = []
        car_data[carCompany][carName].append(carYear)
    
    return car_data

async def get_car_code(db: AsyncSession, carCompany: str, carName: str, carYear: str) -> str | None:
    result: Result = await db.execute(
        select(car_model.Car.carCode).filter(
            car_model.Car.carCompany == carCompany,
            car_model.Car.carName == carName,
            car_model.Car.carYear == carYear
        )
    )
    car_code = result.scalars().first()
    return car_code
