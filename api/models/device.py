from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from api.db import Base


class Device(Base):
    __tablename__ = "devices"

    uid = Column(Integer, primary_key=True, index=True)
    userAgent = Column(String(255), nullable=True)
    carCompany = Column(String(15), nullable=True)
    carName = Column(String(15), nullable=True)
    carYear = Column(String(15), nullable=True)
    carCode = Column(String(10), nullable=True)
    createDttm = Column(DateTime, default=func.now())
    updateDttm = Column(DateTime, default=func.now(), onupdate=func.now())
    
class talkhistory(Base):
    __tablename__ = "talkhistories"

    uid = Column(Integer, ForeignKey("devices.uid"), primary_key=True, index=True)
    talkseq = Column(Integer, primary_key=True, index=True)
    user1text = Column(String(500), nullable=True)
    user2text = Column(String(500), nullable=True)
    createDttm = Column(DateTime, default=func.now())
