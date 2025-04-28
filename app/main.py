from fastapi import FastAPI
import requests
import os

app = FastAPI()

UPSTOX_API_KEY = os.getenv("29293c26-f228-4b54-a52c-2aabd500d385")
UPSTOX_ACCESS_TOKEN = os.getenv("eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI1WEI3RkQiLCJqdGkiOiI2ODBmNmM1ODlkZTNiMjNiZDA2YmM2NTIiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQ1ODQxMjQwLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDU4Nzc2MDB9.fJyHYH_S19GVjfBSJHpXlQ4YxBx-cW_SphIMgUxEDIo")

@app.get("/")
def read_root():
    return {"message": "🚀 Upstox API Server is Running!"}

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
