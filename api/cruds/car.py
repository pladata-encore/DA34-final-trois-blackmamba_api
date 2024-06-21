from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import pytz
import api.models.car as car_model
import api.schemas.car as car_schema

seoul = pytz.timezone('Asia/Seoul')

def get_current_time_in_seoul():
    return datetime.now(seoul)

async def create_car(db: AsyncSession, car_create:car_schema.CarCreate) -> car_model.Car:
    now = get_current_time_in_seoul()
    car_data = car_create.dict(exclude_unset=True)
    car_data.setdefault("isActive", True)
    car_data.setdefault("createDttm", now)
    car_data.setdefault("updateDttm", now)
    car = car_model.Car(**car_data)
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
    car_data = car_create.dict(exclude_unset=True)
    original.carCompany = car_data.get("carCompany", original.carCompany)
    original.carName = car_data.get("carName", original.carName)
    original.carYear = car_data.get("carYear", original.carYear)
    original.carCode = car_data.get("carCode", original.carCode)
    original.isActive = car_data.get("isActive", original.isActive)
    original.updateDttm = get_current_time_in_seoul()
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

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
