import json
import os
import subprocess
import tempfile
from fastapi import APIRouter, File, Request, Depends, HTTPException, UploadFile
from fastapi import params
from fastapi.params import Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
import torch
from fastapi import Response
from transformers import pipeline


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

    userId = request.cookies.get("user_id")

    patient_response = supabase.table("patients").select("*").eq("patientid", userId).single().execute()
    patient = patient_response.data if patient_response.data else {}

    response = supabase.table("mission").select("*").eq("patientId", userId).execute()
    missions = response.data[0]["data"]

    return templates.TemplateResponse("mission.html", {
        "request": request,
        "patient": patient,
        "missions": missions
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


@router.get("/lesson/{assignment_id}")
async def showLession(assignment_id: int, request: Request, resp=Depends(check_patient_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    # Get assignments
    assignment_res = supabase.table("home_assignmentdescription").select("*").eq("assignmentid", assignment_id).execute()
    if not assignment_res.data:
        raise HTTPException(status_code=404, detail="No assignment descriptions found")
    assignments = assignment_res.data

    # Create lesson list
    lessons = []

    for a in assignments:
        template_res = supabase.table("templates").select("*").eq("templateid", a["templateid"]).execute()
        if not template_res.data:
            continue
        template = template_res.data[0]


        activity_res = supabase.table("activities").select("*").eq("activityid", template["activityid"]).execute()
        if not activity_res.data:
            continue
        activity = activity_res.data[0]


        lessons.append({
            "assignment": a,
            "template": template,
            "activity": activity
        })

    # ✅ Create response from TemplateResponse
    response = templates.TemplateResponse("each_lesson.html", {
        "request": request,
        "lessons": lessons
    })
    return response

@router.get("/activity/{activity_id}")
async def showActivity(
    activity_id: int,
    request: Request,
    assignment_id: int = Query(...),
    resp=Depends(check_patient_role)
):
    if isinstance(resp, RedirectResponse):
        return resp

    userId = request.cookies.get("user_id")

    tc_contents = []
    story_data = {}
    if activity_id:
        tc_view_res = supabase.table("tc_view").select("*").eq("activityid", activity_id).eq("assignmentid", assignment_id).execute()
        tc_contents = tc_view_res.data if tc_view_res.data else []

        if tc_contents:
            raw_sentence = tc_contents[0]["sentence"]
            try:
                story_data = json.loads(raw_sentence)
            except Exception as e:
                print("❌ Error parsing sentence JSON:", e)

    file_list = {
        1: "les_listen_speak2.html",
        2: "les_listen_speak.html",
        3: "les_speak_similar.html",
        4: "les_short_story.html",
        5: "les_thinkpic.html",
        6: "les_listen_speak3.html",
        8: "les_seq.html"
    }

    print("tc_contents : ", tc_contents)
    print("story_data : ", story_data)

    return templates.TemplateResponse(file_list[activity_id], {
        "request": request,
        "story_data": story_data,
        "tc_contents": tc_contents,
        "assignment_id": assignment_id
    })


# if 0 = GPU, if can't use GPU, use CPU
device = 0 if torch.cuda.is_available() else "cpu" 
asr = pipeline(
    task="automatic-speech-recognition",
    model="biodatlab/whisper-th-medium-combined",
    chunk_length_s=30,
    device=device
)

@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp_webm:
        temp_webm.write(await file.read())
        webm_path = temp_webm.name

    wav_path = webm_path.replace(".webm", ".wav")
    subprocess.run(["ffmpeg", "-i", webm_path, "-ar", "16000", "-ac", "1", wav_path], check=True)

    result = asr(wav_path, generate_kwargs={"language": "<|th|>", "task": "transcribe"})

    os.remove(webm_path)
    os.remove(wav_path)

    print(f"Transcription result: {result['text']}")

    return {"text": result["text"]}


@router.post("/check_answer/")
async def check_answer(request: Request):
    data = await request.json()
    answer = data.get("answer", "").strip().lower().replace(" ", "")
    word = data.get("word", "").strip().lower()
    print(f"🔍 Checking: '{answer}' vs '{word}'")
    isCorrect = answer == word
    

    if isCorrect:
        return JSONResponse(status_code=200, content={"message": "Correct"})
    else:
        raise HTTPException(status_code=400, detail="Incorrect")

