from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.device as schema
import api.cruds.device as crud
from api.db import get_db

router = APIRouter()

@router.get("/devices", response_model=list[schema.Device])
async def list_devices(db: AsyncSession = Depends(get_db)):
    return await crud.get_devices(db)

@router.post("/devices", response_model=schema.DeviceCreateResponse)
async def create_device(device_body: schema.DeviceCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_device(db, device_body)

@router.put("/devices/{uid}", response_model=schema.DeviceCreateResponse)
async def update_device(uid: int, device_body: schema.DeviceCreate, db: AsyncSession = Depends(get_db)):
    device = await crud.get_device(db, uid=uid)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    
    return await crud.update_device(db, device_body, original=device)

@router.post("/messages", response_model=schema.ChatMessage)
async def create_chat_message(message_body: schema.ChatMessageCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_chat_message(db, message_body)

@router.get("/messages", response_model=list[schema.ChatMessage])
async def list_chat_messages(uid: int, skip: int = 0, limit: int = 30, db: AsyncSession = Depends(get_db)):
    return await crud.get_chat_messages(db, uid=uid, skip=skip, limit=limit)
