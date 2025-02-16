from fastapi import FastAPI
from house import router as house_router
from room import router as room_router
from device import router as device_router
from user import router as user_router

# this script registers routers so they can run on one server
app = FastAPI()
app.include_router(house_router)
app.include_router(room_router)
app.include_router(device_router)
app.include_router(user_router)

# define and run server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

# run with uvicorn main:app --reload
