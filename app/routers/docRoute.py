from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.db.db import supabase

router = APIRouter()
templates = Jinja2Templates(directory="templates")

#^ slp 
@router.get("/", response_class=HTMLResponse)
async def showHome(request: Request):
    response = supabase.table("activities").select("*").execute()
    lessons = response.data
    return templates.TemplateResponse("home_p.html", {
        "request": request,
        "lessons": lessons
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
