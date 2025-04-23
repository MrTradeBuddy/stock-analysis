from fastapi import FastAPI, Request, Form
import requests
import time
import threading
import numpy as np
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# Example Stock List (you can expand or replace based on need)
STOCK_LIST = ["TATAMOTORS", "RELIANCE", "HDFCBANK", "INFY", "ITC"]

# Dummy function simulating API response
# Replace with actual Upstox API logic
def fetch_indicator_data(symbol):
    # Replace this block with actual Upstox API call
    dummy_data = {
        "TATAMOTORS": (42, "Bullish", "Buy", 1032.45),
        "RELIANCE": (48, "Bullish", "Buy", 2924.30),
        "HDFCBANK": (38, "Bearish", "Sell", 1531.75),
        "INFY": (53, "Neutral", "Hold", 1420.10),
        "ITC": (45, "Bullish", "Buy", 425.85)
    }
    return dummy_data.get(symbol, (50, "Neutral", "Hold", 100.00))

@app.get("/", response_class=HTMLResponse)
def home():
    recommended_html = """
    <div style='margin-top:40px;'>
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
        <head><title>BETA - Smart Trade Interface</title>
        <style>
            html, body {{
                height: 100%;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
                font-family: Arial, sans-serif;
                display: flex;
                align-items: flex-start;
                justify-content: center;
                padding-top: 40px;
            }}
            .card {{
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
                text-align: center;
                width: 90%;
                max-width: 500px;
                background: #ffffff;
            }}
            input, button {{
                padding: 12px;
                font-size: 16px;
                margin-top: 12px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }}
            input {{
                width: 100%;
            }}
            button {{
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
            }}
            button:hover {{
                background-color: #45a049;
            }}
        </style>
        </head>
        <body>
            <div class="card">
                <h2>📈 Enter stock like this: <strong>TATAMOTORS</strong></h2>
                <form action="/redirect" method="post">
                    <input name="symbol" placeholder="Enter stock name in English">
                    <br>
                    <button type="submit">Submit</button>
                </form>
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
                <h1>📊 Stock Info: {symbol.upper()}</h1>
                <h2>💰 Price: ₹{ltp:.2f}</h2>
                <p>🔵 RSI: {rsi}</p>
                <p>🟢 EMA Trend: {ema_trend}</p>
                <p>🟩 Supertrend: {supertrend_signal}</p>
                <br>
                <a href="/">🔙 Back</a>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html><body><h3>⚠️ Unable to fetch stock data: {e}</h3><a href='/'>Try Again</a></body></html>
        """
