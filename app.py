from fastapi import FastAPI, Form
import requests
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Sample Stocks List
STOCK_LIST = ["TATAMOTORS", "RELIANCE", "HDFCBANK", "INFY", "ITC"]

# Dummy Stock Data (Replace with Upstox logic)
def fetch_indicator_data(symbol):
    dummy_data = {
        "TATAMOTORS": (42, "Bullish", "Buy", 1032.45),
        "RELIANCE": (48, "Bullish", "Buy", 2924.30),
        "HDFCBANK": (38, "Bearish", "Sell", 1531.75),
        "INFY": (53, "Neutral", "Hold", 1420.10),
        "ITC": (45, "Bullish", "Buy", 425.85)
    }
    return dummy_data.get(symbol, (50, "Neutral", "Hold", 100.00))

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
    data = response.json()

    index_data = {}
    for label, key in index_keys.items():
        info = data["data"][key]
        index_data[label] = {
            "price": info["last_price"],
            "change": info["change"],
            "percent": info["change_percent"]
        }
    return index_data

@app.get("/", response_class=HTMLResponse)
def home():
    access_token = "YOUR_UPSTOX_ACCESS_TOKEN_HERE"  # Replace with valid token
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
        rsi, ema, st, price = fetch_indicator_data(symbol)
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
        <head><title>BETA - Smart Trade Interface</title></head>
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
        rsi, ema_trend, supertrend_signal, ltp = fetch_indicator_data(symbol.upper())

        return f"""
        <html>
            <head><title>{symbol.upper()} - Stock Info</title></head>
            <body style='font-family:sans-serif;text-align:center;background-color:#ffffff;padding:50px;'>
                <h1>📈 Stock Info: {symbol.upper()}</h1>
                <h2>💰 Price: ₹{ltp:.2f}</h2>
                <p>🔵 RSI: {rsi}</p>
                <p>🟢 EMA Trend: {ema_trend}</p>
                <p>🟉 Supertrend: {supertrend_signal}</p>
                <br>
                <a href="/">🖙 Back</a>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html><body><h3>⚠️ Unable to fetch stock data: {e}</h3><a href='/'>Try Again</a></body></html>
        """
