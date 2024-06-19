from fastapi import APIRouter

router = APIRouter()


# @router.get("/talkhistorys")
# async def list_talkhistorys():
#     pass


# @router.post("/devices")
# async def create_devices():
#     pass


@router.put("/devices/{device_id}/talkhistory")
async def update_talkhistory():
    pass


@router.delete("/devices/{device_id}/talkhistory")
async def delete_talkhistory():
    pass