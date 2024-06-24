from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import pytz

import api.models.device as device_model
import api.schemas.device as device_schema

seoul = pytz.timezone('Asia/Seoul')

def get_current_time_in_seoul():
    return datetime.now(seoul)

async def create_device(db: AsyncSession, device_create:device_schema.DeviceCreate) -> device_model.Device:
    now = get_current_time_in_seoul()
    device_data = device_create.dict(exclude_unset=True)
    device_data.setdefault("createDttm", now)
    device_data.setdefault("updateDttm", now)
    device = device_model.Device(**device_data)
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
    device_data = device_create.dict(exclude_unset=True)
    original.userAgent = device_data.get("userAgent", original.userAgent)
    original.cid = device_data.get("cid", original.cid)
    original.updateDttm = get_current_time_in_seoul()    
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

# async def delete_device(db: AsyncSession, original:device_model.Device) -> None:
#     await db.delete(original)
#     await db.commit()