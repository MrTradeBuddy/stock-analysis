from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head><title>Mr. Trade Buddy</title></head>
        <body style='text-align:center;padding:50px;font-family:sans-serif;'>
            <h2>📈 Enter Stock Symbol to Get CMP</h2>
            <form action="/cmp" method="post">
                <input name="symbol" placeholder="e.g. TATAMOTORS" style="padding:10px;width:250px;font-size:16px;">
                <button type="submit" style="padding:10px;font-size:16px;">Get CMP</button>
            </form>
        </body>
    </html>
    """

from fastapi import Form

@app.post("/cmp", response_class=HTMLResponse)
def cmp_result(symbol: str = Form(...)):
    return f"""
    <html>
        <body style='text-align:center;padding:50px;font-family:sans-serif;'>
            <h2>📊 CMP for {symbol.upper()}</h2>
            <h3>Feature Coming Soon 😎</h3>
            <a href="/">🔙 Back</a>
        </body>
    </html>
    """
