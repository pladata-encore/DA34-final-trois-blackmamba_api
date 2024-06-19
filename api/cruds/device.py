from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

import api.models.device as device_model
import api.schemas.device as device_schema

async def create_device(db: AsyncSession, device_create:device_schema.DeviceCreate) -> device_model.Device:
    device = device_model.Device(**device_create.dict())
    db.add(device)
    await db.commit()
    await db.refresh(device)
    return device

async def get_devices(db: AsyncSession) -> list[device_model.Device]:
    result: Result = await db.execute(
        select(
            device_model.Device
        )
    )
    return result.scalars().all()

async def get_device(db: AsyncSession, uid: int) -> device_model.Device | None:
    result: Result = await db.execute(
        select(device_model.Device).filter(device_model.Device.uid == uid)
    )
    return result.scalars().first()

async def update_device(db: AsyncSession, device_create:device_schema.DeviceCreate, original:device_model.Device) -> device_model.Device:
    original.userAgent = device_create.userAgent
    original.carCompany = device_create.carCompany
    original.carName = device_create.carName
    original.carYear = device_create.carYear
    original.carCode = device_create.carCode
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_device(db: AsyncSession, original:device_model.Device) -> None:
    await db.delete(original)
    await db.commit()