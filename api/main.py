from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import device, talk_history, car

app = FastAPI()

app.include_router(device.router)
app.include_router(talk_history.router)
app.include_router(car.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)