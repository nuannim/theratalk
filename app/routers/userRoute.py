from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def showHome(request: Request):
    return templates.TemplateResponse("home_patient.html", {
        "request": request
    })

@router.get("/mission")
async def showMission(request: Request):
    return templates.TemplateResponse("mission.html", {
        "request": request
    })

@router.get("/profile")
async def showProfile(request: Request):
    return templates.TemplateResponse("profile_patient.html", {
        "request": request
    })

@router.get("/lession")
async def showLession(request: Request):
    return templates.TemplateResponse("les_listen_speak.html", {
        "request": request
    })
