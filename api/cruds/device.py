from sqlalchemy import select, desc
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import pytz
import api.models.device as model
import api.schemas.device as schema

seoul = pytz.timezone('Asia/Seoul')

def get_current_time_in_seoul():
    return datetime.now(seoul)

async def create_device(db: AsyncSession, device_create: schema.DeviceCreate) -> model.Device:
    now = get_current_time_in_seoul()
    device_data = device_create.dict(exclude_unset=True)
    device_data.setdefault("createDttm", now)
    device_data.setdefault("updateDttm", now)
    device = model.Device(**device_data)
    db.add(device)
    await db.commit()
    await db.refresh(device)
    return device

async def get_devices(db: AsyncSession) -> list[model.Device]:
    result: Result = await db.execute(
        select(model.Device)
    )
    return result.scalars().all()

async def get_device(db: AsyncSession, uid: int) -> model.Device | None:
    result: Result = await db.execute(
        select(model.Device).filter(model.Device.uid == uid)
    )
    return result.scalars().first()

async def update_device(db: AsyncSession, device_create: schema.DeviceCreate, original: model.Device) -> model.Device:
    device_data = device_create.dict(exclude_unset=True)
    original.userAgent = device_data.get("userAgent", original.userAgent)
    original.cid = device_data.get("cid", original.cid)
    original.updateDttm = get_current_time_in_seoul()    
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def create_chat_message(db: AsyncSession, message_create: schema.ChatMessageCreate) -> model.ChatMessage:
    now = get_current_time_in_seoul()
    message_data = message_create.dict(exclude_unset=True)
    message_data.setdefault("created_at", now)
    message = model.ChatMessage(**message_data)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message

async def get_chat_messages(db: AsyncSession, uid: int, skip: int = 0, limit: int = 30) -> list[model.ChatMessage]:
    result: Result = await db.execute(
        select(model.ChatMessage)
        .filter(model.ChatMessage.uid == uid)
        .order_by(desc(model.ChatMessage.id))  # 여기서 id 컬럼을 역순으로 정렬합니다. 필요에 따라 다른 컬럼으로 변경할 수 있습니다.
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()