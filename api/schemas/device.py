from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class DeviceBase(BaseModel):
    userAgent: Optional[str] = Field(None, example="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    cid: Optional[int] = Field(None, example=1)
    createDttm: Optional[datetime] = Field(None, example="2022-01-01T00:00:00")
    updateDttm: Optional[datetime] = Field(None, example="2022-01-01T00:00:00")

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
    user_id: int
    created_at: datetime
    uid: int

class ChatMessageCreate(ChatMessageBase):
    pass

class ChatMessage(ChatMessageBase):
    id: int

    class Config:
        orm_mode = True
