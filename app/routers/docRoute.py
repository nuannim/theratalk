from fastapi import APIRouter, Request, HTTPException, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.db.db import supabase
from passlib.context import CryptContext

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
        # slp_home = supabase.table("slp_home").select("*").eq('slpid', user_id).execute()
        # data = slp_home.data
        # # print(f"📊📊 data: {data}")

        # unique_patients = {}
        # for item in data:
        #     patient_id = item["patientid"]
        #     if patient_id not in unique_patients:
        #         unique_patients[patient_id] = {
        #             "patientid": patient_id,
        #             "pfirstname": item["pfirstname"],
        #             "plastname": item["plastname"],
        #             "slpfirstname": item["slpfirstname"],
        #             "slplastname": item["slplastname"],
        #             "slpusername": item["slpusername"]
        #         }

        # patients_list = list(unique_patients.values())
        # print(f"📊📊 patient_list: {patients_list}")

        new_slp_home = supabase.table("patients").select("*").eq("slpid", user_id).execute()
        # print("feafeawfeawfewafewfefewfewfewfew:", new_slp_home)

    return templates.TemplateResponse("home_p.html", {
        "request": request,
        # "lessons": lessons,
        "data": new_slp_home.data
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
        # ลืมไปว่า ถ้าslpไม่มีผุ้ป่วยจะไม่แสดงผล
        slp_result = supabase.table("slp").select("*").eq("slpid", user_id).single().execute()
        slp_data = slp_result.data if slp_result.data else {}

        user_id = request.cookies.get("user_id")
        if user_id:
            new_slp_home = supabase.table("patients").select("*").eq("slpid", user_id).execute()
            # print("feafeawfeawfewafewfefewfewfewfew:", new_slp_home)

    return templates.TemplateResponse("profile_p.html", {
        "request": request,
        "data": new_slp_home.data,
        "slp_data": slp_data
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
    response = supabase.table("patients").select("*").eq("patientid", patientid).execute()
    data = response.data

    # print(f"afefpekfewkofekopawfkeoawfe data: {data}")

    return templates.TemplateResponse("assign_p.html", {
        "request": request,
        "data": data
    })

#! ยังไม่เสร็จ
@router.get("/checkmypatient/{patientid}")
async def showCheck(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp

    patientid = request.path_params.get("patientid")
    response = supabase.table("patients").select("*").eq("patientid", patientid).execute()
    data = response.data

    response_assignments = supabase.table("assignments").select("assignmentid, patientid, assignmentdate").eq("patientid", patientid).execute()
    data_assignments = response_assignments.data
    # print('iofeoijaifoeajf DATA_ASSIGNMENTS:', data_assignments)

    return templates.TemplateResponse("checkday_p.html", {
        "request": request,
        "data": data,
        'data_assignments': data_assignments
    })

@router.get("/checkmypatient/{patientid}/{date}")
async def showCheckMyPatient(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    
    patientid = request.path_params.get("patientid")
    response = supabase.table("patients").select("*").eq("patientid", patientid).execute()
    data = response.data


    date = request.path_params.get("date")
    response_assignmenteachday = supabase.table("assignments_with_eachdays2").select("*").eq("patientid", patientid).eq("assignmentdate", date).execute()
    data_assignmenteachday = response_assignmenteachday.data
    # print('oijfewaiojfejiefa data assignments_with_eachdays2:', data_assignmenteachday)
    # print('fjeaiofeaji data:', data)

    return templates.TemplateResponse("check_p.html", {
        "request": request,
        "data": data,
        "date": date,
        'data_assignmenteachday': data_assignmenteachday
        })

@router.get("/checkmypatient/{patientid}/{date}/{ahid}")
async def showCheckMyPatient_ahid(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    
    patientid = request.path_params.get("patientid")
    date = request.path_params.get("date")
    ahid = request.path_params.get("ahid")

    response = supabase.table("history_assignmenteachday_patient_templatecontents").select("*").eq("patientid", patientid).eq("ahid", ahid).execute()
    data = response.data
    print('date jfejaiofejiojiofeajiofejiofewaji:', data)

    response_assignmenteachday = supabase.table("assignments_with_eachdays2").select("*").eq("ahid", ahid).execute()
    data_assignmenteachday = response_assignmenteachday.data
    print('oioioioioioioioioi data assignments_with_eachdays2:', data_assignmenteachday)
    # print('jijijijijijiji data:', data)

    return templates.TemplateResponse("checkdescription_p.html", {
        "request": request,
        "data": data,
        "data_assignmenteachday": data_assignmenteachday,
        "date": date,
        "patientid": patientid
    })

@router.get("/resetpassword/{patientid}")
async def showResetPassword(request: Request, resp=Depends(check_slp_role)):
    if isinstance(resp, RedirectResponse):
        return resp
    
    return templates.TemplateResponse("resetpassword_p.html", {
        "request": request
    })

@router.post("/resetpassword/{patientid}")
async def resetPassword(
    request: Request, 
    patientid: int,
    new_password: str = Form(...)
    ):

    print(f'😭😭😭 @router.post("/resetpassword/{patientid}")')
    print('😭 patientid:', patientid)
    print('😭 new_password:', new_password)


    res = supabase.table("patients") \
        .update({"ppassword": new_password}) \
        .eq("patientid", patientid) \
        .execute()

    print("🔧 update result:", res)

    return RedirectResponse(url="/slp/", status_code=302)


@router.get("/addnewpatient")
async def showAddNewPatient(
    request: Request, 
    resp=Depends(check_slp_role)
):
    if isinstance(resp, RedirectResponse):
        return resp
    
    return templates.TemplateResponse("addnewpatient_p.html", {
        "request": request
    })

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/addnewpatient")
async def addNewPatient(
    request: Request,
    pfirstname: str = Form(...),
    plastname: str = Form(...),
    pbirthday: str = Form(...),
    pusername: str = Form(...),
    ppassword: str = Form(...)
):

    print(f'😭😭😭 @router.post("/addnewpatient")')
    print('😭 pfirstname:', pfirstname)
    print('😭 plastname:', plastname)
    print('😭 pbirthday:', pbirthday)
    print('😭 pusername:', pusername)
    print('😭 ppassword:', ppassword)

    user_id = request.cookies.get("user_id")

    data = {
        "pfirstname": pfirstname,
        "plastname": plastname,
        "pbirthday": pbirthday,
        "pusername": pusername,
        "ppassword": pwd_context.hash(ppassword),
        "slpid": user_id
    }


    try:
        response = supabase.table("patients").insert(data).execute()
        print("✅ Insert success:", response)
    except Exception as e:
        print("❌ Insert error:", e)

    return RedirectResponse(url="/slp/", status_code=302)


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


        for record in assignmenteachdays_records:
            if record["comment"] is None:
                record["comment"] = ""

        print('assignmenteachdays_records:', assignmenteachdays_records)
        
        response = supabase.table("assignmenteachday").insert(assignmenteachdays_records).execute()
        
        print("===== router.post(\"/assign/\") =====")
        print(f"📊📊 patientId: {patientId}, assigned_dates: {assigned_dates}, activity: {activity}, slp_id: {slp_id}")
        return {"message": "Assignments saved successfully"}

    except Exception as e:
        print(f"Error saving assignments: {e}")
        return {"message": f"Error saving assignments: {e}"}, 500

