from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def showHome(request: Request):
    return templates.TemplateResponse("home_p.html", {
        "request": request
    })

@router.get("/progress")
async def showProgress(request: Request):
    return templates.TemplateResponse("progress_p.html", {
        "request": request
    })

@router.get("/profile")
async def showProfile(request: Request):
    return templates.TemplateResponse("profile_p.html", {
        "request": request
    })

@router.get("/lession")
async def showLession(request: Request):
    return templates.TemplateResponse("lession_p.html", {
        "request": request
    })