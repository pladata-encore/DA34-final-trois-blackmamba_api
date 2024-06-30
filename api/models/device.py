from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, JSON, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from api.db import Base

class Device(Base):
    __tablename__ = "devices"

    uid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userAgent = Column(String(200), nullable=True)
    cid = Column(Integer, ForeignKey('cars.cid'))
    createDttm = Column(DateTime, default=func.now())
    updateDttm = Column(DateTime, default=func.now(), onupdate=func.now())

    cars = relationship("Car", back_populates="devices")
    messages = relationship("ChatMessage", back_populates="device")

class ChatMessage(Base):
    __tablename__ = "messages"

    id = Column(Integer, autoincrement=True)
    text = Column(String(500), index=True)
    user_id = Column(Integer, index=True)
    created_at = Column(DateTime, default=func.now())
    uid = Column(Integer, ForeignKey('devices.uid'))

    __table_args__ = (PrimaryKeyConstraint('id', 'uid'),)

    device = relationship("Device", back_populates="messages")
