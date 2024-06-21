from pydantic import BaseModel, Field
from datetime import datetime


class CarBase(BaseModel):
    carCompany: str | None = Field(None, example="Hyundai")
    carName: str | None = Field(None, example="avante")
    carYear: str | None = Field(None, example="2010-2015")
    carCode: str | None = Field(None, example="MD")
    isActive: bool = Field(True, example=True)
    createDttm: datetime | None = Field(None, example="2022-01-01T00:00:00")
    updateDttm: datetime | None = Field(None, example="2022-01-01T00:00:00")

class CarCreate(CarBase):
    pass

class CarCreateResponse(CarCreate):
    cid: int

    class Config:
        orm_mode = True


class Car(CarBase):
    cid: int

    class Config:
        orm_mode = True
