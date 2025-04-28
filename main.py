from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# CORS Allow
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load NSE instruments data
with open("instruments_nse.json", "r") as f:
    instruments = json.load(f)

@app.get("/")
async def root():
    return {"message": "🚀 Upstox Stock Search Server Running!"}

@app.get("/search")
async def search_stocks(q: str = Query("")):
    if not q or len(q) < 2:
        return []
    
    results = []
    query_lower = q.lower()
    for stock in instruments:
        if query_lower in stock["symbol"].lower() or query_lower in stock["name"].lower():
            results.append(stock)
            if len(results) >= 10:
                break

    return results
