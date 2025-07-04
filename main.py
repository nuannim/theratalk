from fastapi import FastAPI, Request
from app.routers import userRoute
from app.routers import docRoute
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(userRoute.router, prefix="/user")
app.include_router(docRoute.router, prefix="/doc")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("test.html", {
        "request": request
    })
