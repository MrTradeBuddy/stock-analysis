from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Static files (CSS, JS) சேர் பண்ணுறது
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates (HTML) சேட் பண்ணுறது
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


