from sqlalchemy import create_engine
from api.models.device import Base as DeviceBase
from api.models.car import Base as CarBase

DB_URL = "mysql+pymysql://root@db:3306/drivetalk?charset=utf8"

engine = create_engine(DB_URL, echo=True)

def reset_database():
    DeviceBase.metadata.drop_all(bind=engine)
    CarBase.metadata.drop_all(bind=engine)
    DeviceBase.metadata.create_all(bind=engine)
    CarBase.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()
