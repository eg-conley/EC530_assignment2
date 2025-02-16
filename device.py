from fastapi import APIRouter
router = APIRouter()

devices = {}

# basic CRUD functions
@router.post("/device")
def create_device(device_id: int, name: str, room: str, device_type: str, settings: dict, status: str):
    devices[device_id] = {"name": name, "room": room, "device_type": device_type, "settings": settings, status: status}
    return {"message": "Device created successfully"}

@router.get("/device/{device_id}")
def find_device(device_id: int):
    return devices.get(device_id, {"error" : "Device not found"})

@router.put("/device/{device_id}")
def update_device(device_id: int, name: str, room: str, device_type: str, settings: dict, status: str):
    if device_id in devices:
        devices[device_id]["name"] = name
        devices[device_id]["room"] = room
        devices[device_id]["device_type"] = device_type
        devices[device_id]["settings"] = settings
        devices[device_id]["status"] = status
        return {"message": "Updated device"}
    return {"message" : "Device not found"}

@router.delete("/device/{device_id}")
def delete_device(device_id: int):
    return devices.pop(device_id, {"error" : "Device not found"})