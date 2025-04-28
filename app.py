from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Home Page
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ API Route for Company Names
@app.get("/get_companies")
async def get_companies():
    companies = [
        "Reliance Industries Limited",
        "Tata Consultancy Services (TCS)",
        "HDFC Bank Limited",
        "ICICI Bank Limited",
        "Infosys Limited",
        "Bharti Airtel Limited",
        "State Bank of India (SBI)",
        "Bajaj Finance Limited",
        "Kotak Mahindra Bank Limited",
        "HCL Technologies Limited",
        "Adani Enterprises Limited",
        "Larsen & Toubro Limited (L&T)",
        "Wipro Limited",
        "Titan Company Limited",
        "Asian Paints Limited",
        "Axis Bank Limited",
        "Sun Pharmaceutical Industries Limited",
        "Tata Steel Limited",
        "Maruti Suzuki India Limited",
        "UltraTech Cement Limited"
    ]
    return JSONResponse(content={"companies": companies})
