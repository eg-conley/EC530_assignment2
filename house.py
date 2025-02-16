from fastapi import APIRouter
router = APIRouter()

houses = {}

# basic CRUD functions
@router.post("/house/")
def create_house(house_id: int, name: str, address: str, gps: list[float], owner: dict, occupants: list[dict]):
    houses[house_id] = {"name": name, "address": address, "gps": gps, "owner": owner, "occupants": occupants}
    return {"message": "House created successfully"}

@router.get("/house/{house_id}")
def find_house(house_id: int):
    return houses.get(house_id, {"error" : "House not found"})

@router.put("/house/{house_id}")
def update_house(house_id: int, name: str, address: str, gps: list[float], owner: dict, occupants: list[dict]):
    if house_id in houses:
        houses[house_id]["name"] = name
        houses[house_id]["address"] = address
        houses[house_id]["gps"] = gps
        houses[house_id]["owner"] = owner
        houses[house_id]["occupants"] = occupants
        return {"message": "House updated successfully"}
    return {"message": "House not found"}

@router.delete("/house/{house_id}")
def delete_house(house_id: int):
    return houses.pop(house_id, {"error" : "House not found"})
