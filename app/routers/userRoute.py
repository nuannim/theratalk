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
    
        # ดึง user_id จาก cookie
    user_id = request.cookies.get("user_id")
    assignments = []
    if user_id:
        # response = supabase.table("assignment_full").select("*").eq("patient_id", user_id).execute()
        # assignments = response.data

        response = supabase.table("home").select("*").eq("patientid", user_id).execute()
        assignments = response.data

        response2 = supabase.table("home_assignmentdescription").select("*").execute()
        assignments_description = response2.data

        # response2 = await db.execute(
        #     text("SELECT * FROM home_assignmentdescription"))
        # assignments_description = [dict(row) for row in response.mappings().all()]

        response3 = supabase.table("assignmentforanotherpage").select("*").eq("patientid", user_id).execute()
        asganotherpage = response3.data
        print("🤓🤓🤓lenasganotherpage:", len(asganotherpage))
        print("🤓🤓🤓lenassignment:", len(assignments))


        print(f"😳😳😳😳 userid: {user_id} \nasganotherpage: {asganotherpage} 😳😳😳😳")  # Debugging line
        print(f"🪲🪲🪲 Assignments for user_id {user_id}: {assignments} 🪲🪲🪲")  # Debugging line

        print(f"🙏🙏🙏 Assignments description: {assignments_description} 🙏🙏🙏")


    return templates.TemplateResponse("home_patient.html", {
        "request": request,
        "assignments": assignments,
        "assignments_description": assignments_description,
        'asganotherpage': asganotherpage
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

    user_id = request.cookies.get("user_id")
    if user_id:
        response3 = supabase.table("assignmentforanotherpage").select("*").eq("patientid", user_id).execute()
        asganotherpage = response3.data

        print("🤓🤓🤓lenasganotherpage:", len(asganotherpage))
        print(f"😳😳😳😳 userid: {user_id} \nasganotherpage: {asganotherpage} 😳😳😳😳")  # Debugging line

    return templates.TemplateResponse("profile_patient.html", {
        "request": request,
        "data": asganotherpage
    })

@router.get("/lesson")
async def showLession(request: Request, resp=Depends(check_patient_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    return templates.TemplateResponse("les_listen_speak.html", {
        "request": request
    })

@router.get("/lesson/{lesson_id}")
async def showLession(lesson_id: int, request: Request, resp=Depends(check_patient_role)):
    file_list = {
        1: "les_listen_speak2.html",
        2: "les_listen_speak.html",
        3: "les_speak_similar.html",
        4: "les_short_story.html",
        5: "les_thinkpic.html",
        6: "les_listen_speak3.html",
        8: "les_seq"
    }
    if isinstance(resp, RedirectResponse):
        return resp
    return templates.TemplateResponse(file_list[lesson_id], {
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
