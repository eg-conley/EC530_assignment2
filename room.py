from fastapi import APIRouter
router = APIRouter()

rooms = {}

# basic CRUD functions
@router.post("/room")
def create_room(room_id: int, name: str, house: str, room_type: str, floor: str, size: int):
    rooms[room_id] = {name: name, house: house, room_type: room_type, floor: floor, size: size}
    return {"message" : "Room created successfully"}

@router.get("/room/{room_id}")
def find_room(room_id: int):
    return rooms.get(room_id, {"error": "Room not found"})

@router.put("/room/{room_id}")
def update_room(room_id: int, name: str, house: str, room_type: str, floor: str, size: int):
    if room_id in rooms:
        rooms[room_id]["name"] = name
        rooms[room_id]["house"] = house
        rooms[room_id]["room_type"] = room_type
        rooms[room_id]["floor"] = floor
        rooms[room_id]["size"] = size
        return {"message" : "Room updated successfully"}
    return {"message" : "Room not found"}

@router.delete("/room/{room_id}")
def delete_room(room_id: int):
    return rooms.pop(room_id, {"error": "Room not found"})