from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from sqlalchemy.orm import relationship

from api.db import Base


class Car(Base):
    __tablename__ = "cars"

    cid = Column(Integer, primary_key=True, index=True, autoincrement=True)
    carCompany = Column(String(15), nullable=True)
    carName = Column(String(15), nullable=True)
    carYear = Column(String(15), nullable=True)
    carCode = Column(String(10), nullable=True)
    isActive = Column(Boolean, default=True)
    createDttm = Column(DateTime, default=func.now())
    updateDttm = Column(DateTime, default=func.now(), onupdate=func.now())

    devices = relationship("Device", back_populates="cars")
