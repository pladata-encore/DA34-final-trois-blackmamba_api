from fastapi import FastAPI
from api.routers import device, talk_history, car

app = FastAPI()
app.include_router(device.router)
app.include_router(talk_history.router)
app.include_router(car.router)