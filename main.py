import uvicorn
from fastapi import FastAPI
from app.database import test_mongo_conn
from app.controllers import userController, userTypeController


app = FastAPI()

app.include_router(userController.router)
app.include_router(userTypeController.router)

if __name__ == '__main__':
    test_mongo_conn()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)