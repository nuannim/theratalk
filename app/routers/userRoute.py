from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
# from supabase import *
from app.db.db import supabase, get_user

#^ patient

router = APIRouter()
templates = Jinja2Templates(directory="templates")

#^ from noeysod - อันนี้เช็ค role
def check_patient_role(request: Request):
    role = request.cookies.get("role")
    if not role:
        return RedirectResponse(url="/login", status_code=302)
    if role == "slp":
        return RedirectResponse(url="/slp/", status_code=302)
    if role != "patient":
        return RedirectResponse(url="/login", status_code=302)
        #* 2
        # raise HTTPException(
        #     status_code=302, 
        #     detail="Redirect", 
        #     headers={"Location": "/slp"}
        # )

#^ เก็บไว้ดูเป็นตัวอย่าง
# @router.get("/")
# async def showHome(request: Request):
#     return templates.TemplateResponse("home_patient.html", {
#         "request": request
#     })

#* 2
# @router.get("/")
# async def showHome(request: Request, _: None = Depends(check_patient_role)):
#     return templates.TemplateResponse("home_patient.html", {
#         "request": request
#     })

@router.get("/")
async def showHome(request: Request, resp=Depends(check_patient_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    return templates.TemplateResponse("home_patient.html", {
        "request": request
    })

@router.get("/mission")
async def showMission(request: Request, resp=Depends(check_patient_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    return templates.TemplateResponse("mission.html", {
        "request": request
    })

@router.get("/profile")
async def showProfile(request: Request, resp=Depends(check_patient_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    return templates.TemplateResponse("profile_patient.html", {
        "request": request
    })

@router.get("/lesson")
async def showLession(request: Request, resp=Depends(check_patient_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    return templates.TemplateResponse("les_listen_speak.html", {
        "request": request
    })

# ! เดี๋ยวนะ อันนี้คือไรนะ
# @router.get("/lesson")
# async def showLession(request: Request, resp=Depends(check_patient_role)):
#     if isinstance(resp, RedirectResponse):
#         return resp

#     # ดึง user_id จาก cookie
#     user_id = request.cookies.get("user_id")
#     # ตัวอย่าง: ดึงข้อมูล lesson ของ patient จาก database
#     lessons_response = None
#     lessons = []
#     if user_id:
#         lessons_response = supabase.table("lessons").select("*").eq("patient_id", user_id).execute()
#         lessons = lessons_response.data if lessons_response and lessons_response.data else []

#     return templates.TemplateResponse("les_listen_speak.html", {
#         "request": request,
#         "lessons": lessons
#     })
