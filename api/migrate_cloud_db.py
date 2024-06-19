from sqlalchemy.exc import InternalError, OperationalError
from sqlalchemy import create_engine, text

from api.models.device import Base as DeviceBase
from api.models.car import Base as CarBase
from api.db import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

DB_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?charset=utf8"
DRIVETALK_DB_URL = (
    f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/drivetalk?charset=utf8"
)

engine = create_engine(DRIVETALK_DB_URL, echo=True)

def database_exists():
    try:
        engine.connect()
        return True
    except (OperationalError, InternalError) as e:
        print(e)
        print("database does not exist")
        return False
    

def create_database():
    if not database_exists():
        root = create_engine(DB_URL, echo=True)
        with root.connect() as conn:
            conn.execute(text("CREATE DATABASE drivetalk"))
        print("create database")
    
    DeviceBase.metadata.create_all(bind=engine)
    CarBase.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
