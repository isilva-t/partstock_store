from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client.online_catalog


@app.get("/")
async def root():
    return {"message": "API Catálogo"}


@app.get("/api/search")
async def search(q: str = ""):
    """
    Search endpoint
    """
    return {
        "query": q,
        "results": {},
        "total": 0
    }


@app.on_event("startup")
async def startup_event():
    print("FastAPI started")
    print(f"Connected to MongoDB at {MONGO_URL}")


@app.on_event("shutdown")
async def shutdown_event():
    client.close()
