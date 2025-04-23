from fastapi import FastAPI, Request, Form
import requests
import time
import threading
import numpy as np
from upstox_api.api import Upstox, LiveFeedType
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Mr. Trade Buddy - Web CMP</title></head>
        <body style='font-family:sans-serif;text-align:center;background-color:#f1f1f1;padding:50px;'>
            <h2>📈 பங்குCMP காண</h2>
            <form action="/cmp" method="post">
                <input name="symbol" placeholder="பங்கு பெயரை தமிழில்/ஆங்கிலத்தில் உள்ளிடவும்" style="padding:10px;width:250px;font-size:16px;">
                <button type="submit" style="padding:10px;font-size:16px;">காண்பிக்கவும்</button>
            </form>
        </body>
    </html>
    """

@app.post("/cmp", response_class=HTMLResponse)
def cmp_result(symbol: str = Form(...)):
    try:
        instrument = f"NSE_EQ|{symbol.upper()}"
        price_data = u.get_live_feed(instrument, LiveFeedType.MARKET_DATA)
        ltp = price_data.get('ltp', 0.0)
        rsi = 42.3  # Dummy for UI, replace with actual logic
        ema_trend = "Bullish"  # Dummy for UI, replace with actual logic
        supertrend_signal = "Buy"  # Dummy for UI, replace with actual logic

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

@app.post("/")
async def telegram_webhook(req: Request):
    data = await req.json()
    message = data.get("message", {})
    text = message.get("text", "")
    chat_id = message.get("chat", {}).get("id")

    if text.strip() == "/start":
        send_message(chat_id, "👋 Hello Mr. Buddy! Welcome to the stock bot world 💼📈")
    elif text.startswith("/stock"):
        parts = text.strip().split()
        if len(parts) >= 2:
            symbol = "".join(parts[1:]).replace(" ", "").upper()
            stock_info = get_stock_price(symbol)
            if stock_info:
                send_message(chat_id, f"📊 {symbol}: ₹{stock_info['price']} ({stock_info['change']})")
            else:
                send_message(chat_id, f"❌ Unable to fetch data for {symbol}. Try NSE symbols like RELIANCE, ICICIBANK")
        else:
            send_message(chat_id, "⚠️ Format: /stock SYMBOL\nExample: /stock tatamotors")
    elif text.startswith("/signal"):
        parts = text.strip().split()
        if len(parts) >= 2:
            symbol = "".join(parts[1:]).upper()
            try:
                signal = get_signal_status(symbol)
                send_message(chat_id, signal, markdown=True)
            except Exception as e:
                send_message(chat_id, f"❌ Unable to fetch signal for {symbol}", markdown=True)
        else:
            send_message(chat_id, "⚠️ Format: /signal SYMBOL\nExample: /signal tatamotors", markdown=True)
    else:
        send_message(chat_id, "🤖 Unknown command. Try /start or /stock tata")

# Global tracker to avoid duplicate replies
last_called = {}

# Telegram Bot Details
BOT_TOKEN = "7551804667:AAGcSYXvvHwlv9fWx1rQQM3lQT-mr7bvye8"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Upstox API Setup
API_KEY = "29293c26-f228-4b54-a52c-2aabd500d385"
API_SECRET = "3o5mdjiqcd"
ACCESS_TOKEN = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI1WEI3RkQiLCJqdGkiOiI2ODA4YWU3YTMwYmMxMjBlYTZlNTczODMiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaWF0IjoxNzQ1Mzk5NDE4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NDU0NDU2MDB9.x49jmFTZC9OHSmmbN_cqJYPDgoMbyRBwFj-A49b8ar8"

u = Upstox(API_KEY, API_SECRET)
u.set_access_token(ACCESS_TOKEN)

def get_signal_status(symbol):
    try:
        instrument = f"NSE_EQ|{symbol.upper()}"
        price_data = u.get_live_feed(instrument, LiveFeedType.MARKET_DATA)
        ltp = price_data.get('ltp', 0.0)
        return f"📊 {symbol}\nCMP: ₹{ltp:.2f}"
    except Exception as e:
        print(f"❌ Error in signal generation for {symbol}:", e)
        return "⚠️ Unable to fetch CMP for this stock."

def get_stock_price(symbol):
    try:
        instrument = f"NSE_EQ|{symbol.upper()}"
        price_data = u.get_live_feed(instrument, LiveFeedType.MARKET_DATA)
        ltp = price_data.get('ltp', 0.0)
        prev = price_data.get('close', 0.0)
        change = ((ltp - prev) / prev) * 100 if prev else 0
        arrow = '▲' if change > 0 else '▼' if change < 0 else ''
        return {"price": f"{ltp:.2f}", "change": f"{arrow} {change:.2f}%"}
    except:
        return None

def send_message(chat_id, text, markdown=False):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    if markdown:
        payload["parse_mode"] = "Markdown"
    requests.post(TELEGRAM_API_URL, json=payload)
