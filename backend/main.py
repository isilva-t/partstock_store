from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from constants import Env
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[Env.ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = Env.MONGO_URL
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
