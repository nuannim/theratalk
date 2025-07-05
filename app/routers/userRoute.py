from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

#^ patient

router = APIRouter()
templates = Jinja2Templates(directory="templates")

#^ from noeysod - อันนี้เช็ค role
def check_patient_role(request: Request):
    role = request.cookies.get("role")
    if role != "patient":
        raise HTTPException(
            status_code=302, 
            detail="Redirect", 
            headers={"Location": "/slp"}
        )

#^ เก็บไว้ดูเป็นตัวอย่าง
# @router.get("/")
# async def showHome(request: Request):
#     return templates.TemplateResponse("home_patient.html", {
#         "request": request
#     })

@router.get("/")
async def showHome(request: Request, _: None = Depends(check_patient_role)):
    return templates.TemplateResponse("home_patient.html", {
        "request": request
    })

@router.get("/mission")
async def showMission(request: Request, _: None = Depends(check_patient_role)):
    return templates.TemplateResponse("mission.html", {
        "request": request
    })

@router.get("/profile")
async def showProfile(request: Request, _: None = Depends(check_patient_role)):
    return templates.TemplateResponse("profile_patient.html", {
        "request": request
    })

@router.get("/lession")
async def showLession(request: Request, _: None = Depends(check_patient_role)):
    return templates.TemplateResponse("les_listen_speak.html", {
        "request": request
    })
