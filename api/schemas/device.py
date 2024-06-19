from pydantic import BaseModel, Field


class DeviceBase(BaseModel):
    userAgent: str | None = Field(None, example="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    carCompany: str | None = Field(None, example="Hyundai")
    carName: str | None = Field(None, example="avante")
    carYear: str | None = Field(None, example="2010-2015")
    carCode: str | None = Field(None, example="MD")


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

class CarBase(BaseModel):
    carCompany: str | None = Field(None, example="Hyundai")
    carName: str | None = Field(None, example="avante")
    carYear: str | None = Field(None, example="2010-2015")
    carCode: str | None = Field(None, example="MD")
    isActive: bool = Field(True, description="서비스 사용 여부") 


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
