from fastapi import FastAPI
from routes.users import router as user_router
from routes.main import router as main_router

app = FastAPI()
prefix = "/api/v1"
app.include_router(main_router, prefix=prefix, tags=["Main"])
app.include_router(user_router, prefix=prefix, tags=["Users"])

# uvicorn main:app --reload   -> to run the server
