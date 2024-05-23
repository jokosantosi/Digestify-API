from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

@app.get('/')
async def root():
    return {"status": 200, "message": ["Server is Running!"]}

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["GET", "POST"],
#     allow_headers=["*"],
# )

@app.get('/api/get-latest-news')
async def getLatestNews():
    with open("dummyDB.json", "r") as f:
        database = json.load(f)
    
    latestNews = {
        "status": 200,
        "message": [],
        "data": database["database"],
        "pagination": {
            "page": 0,
            "total_items": 10,
        }
    }
    return latestNews