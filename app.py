from fastapi import FastAPI, Form
import requests
from fastapi.responses import HTMLResponse, RedirectResponse
import random

app = FastAPI()

# Sample Stocks List
STOCK_LIST = ["TATAMOTORS", "RELIANCE", "HDFCBANK", "INFY", "ITC"]

# Upstox Index Data Fetcher

def get_upstox_indices(access_token):
    base_url = "https://api.upstox.com/v2/market/quote/ltp"
    index_keys = {
        "NIFTY 50": "NSE_INDEX|Nifty 50",
        "BANKNIFTY": "NSE_INDEX|Bank Nifty",
        "SENSEX": "BSE_INDEX|Sensex",
        "GIFT NIFTY": "NSE_INDEX|Gift Nifty"
    }

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    joined_keys = ",".join(index_keys.values())
    url = f"{base_url}?instrument_key={joined_keys}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {}
    data = response.json()

    index_data = {}
    for label, key in index_keys.items():
        try:
            info = data["data"][key]
            index_data[label] = {
                "price": info.get("last_price", 0),
                "change": info.get("change", 0),
                "percent": info.get("change_percent", 0)
            }
        except KeyError:
            index_data[label] = {"price": 0, "change": 0, "percent": 0}
    return index_data

# Fetch Real Stock Data

def fetch_indicator_data(symbol, access_token):
    try:
        url = f"https://api.upstox.com/v2/market/quote/ltp?instrument_key=NSE_EQ|{symbol.upper()}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            raise Exception("Upstox API Error!")
        data = res.json()
        if f"NSE_EQ|{symbol.upper()}" not in data.get("data", {}):
            raise Exception("Invalid Symbol or No Data")

        ltp = data["data"][f"NSE_EQ|{symbol.upper()}"]["last_price"]

        dummy_rsi = random.randint(40, 65)
        dummy_ema = "Bullish" if dummy_rsi > 50 else "Neutral"
        dummy_supertrend = "Buy" if dummy_rsi > 50 else "Hold"

        return dummy_rsi, dummy_ema, dummy_supertrend, ltp

    except Exception as e:
        print(f"Error fetching real data for {symbol}: {e}")
        return 50, "Neutral", "Hold", 100.00

@app.get("/", response_class=HTMLResponse)
def home():
    access_token = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI1WEI3RkQiLCJqdGkiOiI2ODBiODM4OTFmNWE4MTAzMjA2OTUxY2YiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQ1NTg1MDMzLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDU2MTg0MDB9.poBbU-KCJNxfV-4n6W0q7LRU9h2gfyF2_hMgI3ah-_Y"
    index_data = get_upstox_indices(access_token)

    index_html = "<div style='margin-bottom:30px;'>"
    for name, data in index_data.items():
        color = "#e53935" if data['change'] < 0 else "#43a047"
        index_html += f"""
        <div style='display:inline-block; border:1px solid #ccc; padding:10px 14px; border-radius:8px; margin:5px;'>
            <strong>{name}</strong><br>
            ₹{data['price']} <span style='color:{color};'>({data['percent']}%)</span>
        </div>
        """
    index_html += "</div>"

    recommended_html = """
    <div style='margin-top:20px;'>
        <h3 style='text-align:center;'>🔥 Recommended Stocks</h3>
        <div style='display: flex; flex-direction: column; gap: 10px; align-items: center;'>
    """
    for symbol in STOCK_LIST:
        rsi, ema, st, price = fetch_indicator_data(symbol, access_token)
        emoji = "📈" if st == "Buy" else "📉" if st == "Sell" else "💹"
        recommended_html += f"""
        <div style='border:1px solid #ddd;padding:10px 20px;border-radius:8px;width:100%;max-width:400px;'>
            {emoji} <strong>{symbol}</strong><br>
            💰 Price: ₹{price} <br>
            RSI: {rsi} | EMA: {ema} | Supertrend: {st}
        </div>
        """
    recommended_html += "</div></div>"

    return f"""
    <html>
        <head>
            <title>BETA - Smart Trade Interface</title>
            <meta http-equiv="refresh" content="5">
        </head>
        <body style='font-family:Arial, sans-serif; padding: 40px;'>
            <div class="card">
                <h2>📈 Enter stock like this: <strong>TATAMOTORS</strong></h2>
                <form action="/redirect" method="post">
                    <input name="symbol" placeholder="Enter stock name" style='padding:12px;width:100%;max-width:400px;'>
                    <br><br>
                    <button type="submit" style='padding:12px 24px;background:#4CAF50;color:white;border:none;border-radius:6px;'>Submit</button>
                </form>
                {index_html}
                {recommended_html}
            </div>
        </body>
    </html>
    """

@app.post("/redirect")
def redirect_to_cmp(symbol: str = Form(...)):
    return RedirectResponse(url=f"/cmp/{symbol.upper()}", status_code=302)

@app.get("/cmp/{symbol}", response_class=HTMLResponse)
def show_cmp(symbol: str):
    try:
        access_token = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI1WEI3RkQiLCJqdGkiOiI2ODBiODM4OTFmNWE4MTAzMjA2OTUxY2YiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQ1NTg1MDMzLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDU2MTg0MDB9.poBbU-KCJNxfV-4n6W0q7LRU9h2gfyF2_hMgI3ah-_Y"
        rsi, ema_trend, supertrend_signal, ltp = fetch_indicator_data(symbol.upper(), access_token)

        return f"""
        <html>
            <head><title>{symbol.upper()} - Stock Info</title><meta http-equiv="refresh" content="5"></head>
            <body style='font-family:sans-serif;text-align:center;background-color:#ffffff;padding:50px;'>
                <h1>📈 Stock Info: {symbol.upper()}</h1>
                <h2>💰 Price: ₹{ltp:.2f}</h2>
                <p>🔵 RSI: {rsi}</p>
                <p>🟢 EMA Trend: {ema_trend}</p>
                <p>🟩 Supertrend: {supertrend_signal}</p>
                <br>
                <a href="/">🖙 Back</a>
            </body>
        </html>
        """
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"""
        <html><body><h3>⚠️ Unable to fetch stock data: {e}</h3><a href='/'>Try Again</a></body></html>
        """
