from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db.db import supabase

#^ slp 

router = APIRouter()
templates = Jinja2Templates(directory="templates")

#^ from noeysod - อันนี้เช็ค role
# def check_slp_role(request: Request):
#     role = request.cookies.get("role")
#     if role != "slp":
#         raise HTTPException(
#             status_code=302, 
#             detail="Redirect", 
#             headers={"Location": "/patient"}
#         )
    
def check_slp_role(request: Request):
    role = request.cookies.get("role")
    if not role:
        return RedirectResponse(url="/login", status_code=302)
    if role == "patient":
        return RedirectResponse(url="/patient/", status_code=302)
    if role != "slp":
        return RedirectResponse(url="/login", status_code=302)

# @router.get("/", response_class=HTMLResponse)
# async def showHome(request: Request):
#     response = supabase.table("activities").select("*").execute()
#     lessons = response.data
#     return templates.TemplateResponse("home_p.html", {
#         "request": request,
#         "lessons": lessons
#     })

@router.get("/", response_class=HTMLResponse)
async def showHome(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    
    response = supabase.table("activities").select("*").execute()
    lessons = response.data
    return templates.TemplateResponse("home_p.html", {
        "request": request,
        "lessons": lessons
    })

@router.get("/progress")
async def showProgress(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    return templates.TemplateResponse("progress_p.html", {
        "request": request
    })

@router.get("/profile")
async def showProfile(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    return templates.TemplateResponse("profile_p.html", {
        "request": request
    })

@router.get("/lesson")
async def showLession(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    return templates.TemplateResponse("lession_p.html", {
        "request": request
    })
