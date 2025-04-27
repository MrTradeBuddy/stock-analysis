from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/market-data")
async def get_market_data():
    # 👉 Here connect to Upstox API and fetch real-time data
    return JSONResponse({
        "nifty": {"price": 22450.55, "status": "✅ Stable"},
        "banknifty": {"price": 47850.00, "status": "📈 Rising"},
        "sensex": {"price": 74000.40, "status": "📉 Falling"}
    })
