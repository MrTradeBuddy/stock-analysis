from fastapi import FastAPI, Request, Form
import requests
import time
import threading
import numpy as np
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>BETA - Smart Trade Interface</title>
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
                background-color: #ffffff;
                font-family: Arial, sans-serif;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
            }
            .card {
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
                text-align: center;
                width: 90%;
                max-width: 400px;
                background: #ffffff;
            }
            input, button {
                padding: 12px;
                font-size: 16px;
                margin-top: 12px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }
            input {
                width: 100%;
            }
            button {
                background-color: #4CAF50;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
        </style>
        </head>
        <body>
            <div class="card">
                <h2>📈 Enter stock like this: TATAMOTORS</h2>
                <form action="/redirect" method="post">
                    <input name="symbol" placeholder="Enter stock name in English">
                    <br>
                    <button type="submit">Submit</button>
                </form>
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
        ltp = 972.50
        rsi = 42.3
        ema_trend = "Bullish"
        supertrend_signal = "Buy"

        return f"""
        <html>
            <head><title>{symbol.upper()} - Stock Info</title></head>
            <body style='font-family:sans-serif;text-align:center;background-color:#fff;padding:50px;'>
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
