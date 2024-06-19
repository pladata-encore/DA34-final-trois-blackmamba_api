from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.device as device_schema
import api.cruds.device as device_crud
from api.db import get_db

router = APIRouter()


@router.get("/devices", response_model=list[device_schema.Device])
async def list_devices(db: AsyncSession = Depends(get_db)):
    return await device_crud.get_devices(db)


@router.post("/devices", response_model=device_schema.DeviceCreateResponse)
async def create_device(device_body: device_schema.DeviceCreate, db: AsyncSession = Depends(get_db)):
    return await device_crud.create_device(db, device_body)


@router.put("/devices/{uid}", response_model=device_schema.DeviceCreateResponse)
async def update_device(uid:int, device_body: device_schema.DeviceCreate, db: AsyncSession = Depends(get_db)):
    device = await device_crud.get_device(db, uid=uid)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    
    return await device_crud.update_device(db, device_body, original=device)


@router.delete("/devices/{uid}", response_model=None)
async def delete_device(uid:int, db: AsyncSession = Depends(get_db)):
    device = await device_crud.get_device(db, uid=uid)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    
    return await device_crud.delete_device(db, original=device)
