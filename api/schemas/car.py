from pydantic import BaseModel, Field


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
