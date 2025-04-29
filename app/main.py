from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# ✅ Enable CORS for all origins (can restrict to specific domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["https://opthub.onrender.com"] to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API Credentials from environment variables
UPSTOX_API_KEY = os.getenv("29293c26-f228-4b54-a52c-2aabd500d385")
UPSTOX_ACCESS_TOKEN = os.getenv("eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ...")

# ✅ Static Stock List
stocks = [
    {"symbol": "RELIANCE", "name": "Reliance Industries"},
    {"symbol": "TCS", "name": "Tata Consultancy Services"},
    {"symbol": "INFY", "name": "Infosys Limited"},
    {"symbol": "ICICIBANK", "name": "ICICI Bank"},
    {"symbol": "HDFCBANK", "name": "HDFC Bank"},
    {"symbol": "SBIN", "name": "State Bank of India"},
    {"symbol": "AXISBANK", "name": "Axis Bank"},
    {"symbol": "KOTAKBANK", "name": "Kotak Mahindra Bank"},
    {"symbol": "ITC", "name": "ITC Limited"},
    {"symbol": "LT", "name": "Larsen & Toubro"},
]

@app.get("/")
def read_root():
    return {"message": "🚀 Upstox API Server is Running!"}

# ✅ Live Price API
@app.get("/liveprice/{symbol}")
def get_live_price(symbol: str):
    headers = {
        "x-api-key": UPSTOX_API_KEY,
        "Authorization": f"Bearer {UPSTOX_ACCESS_TOKEN}"
    }
    url = f"https://api.upstox.com/v2/market-quote/ltp?symbol=NSE_EQ:{symbol}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        try:
            ltp = data['data'][f'NSE_EQ:{symbol}']['last_price']
            return {"symbol": symbol, "ltp": ltp}
        except KeyError:
            return {"error": "Symbol data not found!"}
    else:
        return {"error": response.text}

# ✅ Smart Search API
@app.get("/search")
def search_stocks(q: str):
    q_lower = q.lower()
    results = [
        stock for stock in stocks
        if stock["symbol"].lower().startswith(q_lower) or q_lower in stock["name"].lower()
    ]
    return results
