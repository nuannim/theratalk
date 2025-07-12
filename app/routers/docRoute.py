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
    
    # response = supabase.table("activities").select("*").execute()
    # lessons = response.data
    # print (f"😭😭 lesson: {lessons}")
    user_id = request.cookies.get("user_id")
    if user_id:
        slp_home = supabase.table("slp_home").select("*").eq('slpid', user_id).execute()
        data = slp_home.data
        # print(f"📊📊 data: {data}")

        unique_patients = {}
        for item in data:
            patient_id = item["patientid"]
            if patient_id not in unique_patients:
                unique_patients[patient_id] = {
                    "patientid": patient_id,
                    "pfirstname": item["pfirstname"],
                    "plastname": item["plastname"],
                    "slpfirstname": item["slpfirstname"],
                    "slplastname": item["slplastname"],
                    "slpusername": item["slpusername"]
                }

        patients_list = list(unique_patients.values())
        print(f"📊📊 patient_list: {patients_list}")

    return templates.TemplateResponse("home_p.html", {
        "request": request,
        # "lessons": lessons,
        "data": patients_list
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
    
    user_id = request.cookies.get("user_id")
    if user_id:
        slp_home = supabase.table("slp_home").select("*").eq('slpid', user_id).execute()
        data = slp_home.data
        # print(f"📊📊 data: {data}")

        #! ถ้าข้อมูลเยอะ ๆ ไม่ค่อยเหมาะเท่าไหร่
        unique_patients = {}
        for item in data:
            patient_id = item["patientid"]
            if patient_id not in unique_patients:
                unique_patients[patient_id] = {
                    "patientid": patient_id,
                    "pfirstname": item["pfirstname"],
                    "plastname": item["plastname"],
                    "slpfirstname": item["slpfirstname"],
                    "slplastname": item["slplastname"],
                    "slpusername": item["slpusername"]
                }

        patients_list = list(unique_patients.values())
        print(f"📊📊 patient_list: {patients_list}")


    return templates.TemplateResponse("profile_p.html", {
        "request": request,
        "data": patients_list
    })

# ไม่ใช้แล้ว
# @router.get("/lesson")
# async def showLession(request: Request, resp=Depends(check_slp_role)):
#     if isinstance(resp, RedirectResponse):
#         return resp

#     return templates.TemplateResponse("lession_p.html", {
#         "request": request
#     })

@router.get("/mypatient/{patientid}")
async def showMyPatient(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    patientid = request.path_params.get("patientid")
    # response = supabase.table("patients").select("*").execute()
    # data = response.data

    # print(f"📊📊 data: {data}")

    return templates.TemplateResponse("assign_p.html", {
        "request": request
        # ,
        # "data": data
    })

@router.get("/checkmypatient/{patientid}")
async def showCheck(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    patientid = request.path_params.get("patientid")

    return templates.TemplateResponse("check_p.html", {
        "request": request
    })

@router.post("/assign/")
async def assignLesson(
    request: Request,
):
    data = await request.json()

    patientId = data.get("patientId")
    assigned_dates = data.get("assigned_dates")
    activity = data.get("activity")

    slp_id = request.cookies.get("user_id")

    records_to_insert = []

    # for date_str in assigned_dates:
    #     records_to_insert.append({
    #         "patientid": patientId,
    #         "slpid": slp_id,
    #         "assignmentdate": date_str,
    #         "isdone": False,
    #         "assignmentgroupid": None
    #     })
    
    # #! ยังไม่ครบทุกตาราง
    # #response = supabase.table("assignments").insert(records_to_insert).execute()
    
    # print("===== router.post(\"/assign/\") =====")
    # print(f"📊📊 patientId: {patientId}, assigned_dates: {assigned_dates}, activity: {activity}, slp_id: {slp_id}")
    # return {"message": "Assignments saved successfully"}

    from datetime import datetime
    import uuid

    assignment_group_id = str(uuid.uuid4())
    current_time = datetime.now().isoformat()

    try:
        # Insert into assignments table
        assignment_records = []
        for date_str in assigned_dates:
            assignment_records.append({
                "patientid": patientId,
                "slpid": slp_id,
                "assignmentdate": date_str,
                "isdone": False,
                "assignmentgroupid": assignment_group_id,
                "created_at": current_time
            })

        print('assignment_record:', assignment_records)  # * ถูก

        response_assignments = supabase.table("assignments").insert(assignment_records).execute()
        assignments_data = response_assignments.data
        # print('response_assignments:', response_assignments)
        # print('response_assignments.data:', response_assignments.data)
        print('assignments_data:', assignments_data)

        # Insert into assignmenteachdays table
        assignmenteachdays_records = []
        for assignment in assignments_data:
            assignment_id = assignment["assignmentid"]
            # assignmenteachdays_records.append({
            #     "assignmentid": assignment_id,
            #     "templateid": activity, # Assuming 'activity' is the templateid
            #     "isdone": False,
            #     "retries": 0,
            #     "comment": None
            # })
            for template_item in activity:
                assignmenteachdays_records.append({
                    "assignmentid": assignment_id,
                    "templateid": template_item["templateid"],
                    "isdone": False,
                    "retries": 0,
                    "comment": None
                })




        print('assignmenteachdays_records:', assignmenteachdays_records)
        
        for i in assignmenteachdays_records:
            response_assignmenteachdays = supabase.table("assignmenteachdays").insert(i).execute()
            print('response_assignmenteachdays:', response_assignmenteachdays)

        
        print("===== router.post(\"/assign/\") =====")
        print(f"📊📊 patientId: {patientId}, assigned_dates: {assigned_dates}, activity: {activity}, slp_id: {slp_id}")
        return {"message": "Assignments saved successfully"}

    except Exception as e:
        print(f"Error saving assignments: {e}")
        return {"message": f"Error saving assignments: {e}"}, 500

