from fastapi import FastAPI
from database import init_db, close_db
from routers import user_router

app = FastAPI()

# Include routers
app.include_router(user_router.router)

@app.on_event("startup")
async def startup():
    await init_db()  # Connect to DB

@app.on_event("shutdown")
async def shutdown():
    await close_db()  # Close DB connection

# Run: uvicorn main:app --reload
