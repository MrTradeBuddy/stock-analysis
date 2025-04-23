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
        <head><title>Mr. Trade Buddy - Web CMP</title>
        <style>
            body {
                font-family: sans-serif;
                margin: 0;
                background-color: #f1f1f1;
                padding: 50px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .form-container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
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
                <h2>📈 பங்குCMP காண</h2>
                <form action="/cmp" method="post">
                    <input name="symbol" placeholder="பங்கு பெயரை தமிழில்/ஆங்கிலத்தில் உள்ளிடவும்">
                    <br>
                    <button type="submit">காண்பிக்கவும்</button>
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
            <head><title>CMP for {symbol.upper()}</title></head>
            <body style='font-family:sans-serif;text-align:center;background-color:#fff;padding:50px;'>
                <h1>📊 CMP for {symbol.upper()}</h1>
                <h2>💰 Current Price (CMP): ₹{ltp:.2f}</h2>
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
        <html><body><h3>⚠️ பங்கு தகவலை பெற முடியவில்லை: {e}</h3><a href='/'>மீண்டும் முயற்சிக்கவும்</a></body></html>
        """
