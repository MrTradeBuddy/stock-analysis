from fastapi import FastAPI, Request, Form
import requests
import time
import threading
import numpy as np
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Mr. Trade Buddy - Stock Signal Tool</title>
        <style>
            html, body {
                height: 100%;
                margin: 0;
                padding: 0;
                background-color: white;
                font-family: sans-serif;
            }
            .form-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
                position: absolute;
                top: 20%;
                left: 50%;
                transform: translate(-50%, -20%);
            }
            input, button {
                padding: 10px;
                font-size: 16px;
                margin-top: 10px;
            }
            input {
                width: 250px;
            }
        </style>
        </head>
        <body>
            <div class="form-container">
                <h2>📈 Enter stock like this: TATAMOTORS</h2>
                <form action="/cmp" method="post">
                    <input name="symbol" placeholder="Enter stock name in English">
                    <br>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </body>
    </html>
    """

@app.post("/cmp", response_class=HTMLResponse)
def cmp_result(symbol: str = Form(...)):
    try:
        # TEMP FIX: Using dummy CMP value
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
