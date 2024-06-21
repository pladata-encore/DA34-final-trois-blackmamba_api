from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class DeviceBase(BaseModel):
    userAgent: List[str] | None = Field(None, example=["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"])
    cid: int
    createDttm: datetime
    updateDttm: datetime


class DeviceCreate(DeviceBase):
    pass


class DeviceCreateResponse(DeviceCreate):
    uid: int

    class Config:
        orm_mode = True


class Device(DeviceBase):
    uid: int

    class Config:
        orm_mode = True


class ChatMessageBase(BaseModel):
    text: str
    userId: int
    createdDttm: datetime
    uid: int
    

class ChatMessageCreate(ChatMessageBase):
    pass

class ChatMessage(ChatMessageBase):
    mid: int

    class Config:
        orm_mode = True
