from fastapi import FastAPI, Request, Form, Depends
from app.routers import userRoute
from app.routers import docRoute
from fastapi.middleware import Middleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.db import supabase #, get_user, get_db
import jwt
# from db import get_user
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse, JSONResponse

# middleware=[Middleware(AuthMiddleware)]
app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(userRoute.router, prefix="/patient")
app.include_router(docRoute.router, prefix="/slp")

app.mount("/static", StaticFiles(directory="static"), name="static")

# from app.db import models, schemas, crud
# from app.db.db import engine, get_db
# from sqlalchemy.orm import Session

# @app.get("/kuy", response_model=list[schemas.Patient])
# def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     patients = crud.get_patients(db, skip=skip, limit=limit)
#     return patients

@app.get("/")
async def root(request: Request):
    # get_db()
    return templates.TemplateResponse("test.html", {
        "request": request
    })

# ^ from noeysod
@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("testlogin.html", {
        "request": request
        })

# ^ from noeysod
@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    # & just for checking
    print(f"😭😭😭 Username: {username}, Password: {password}")

    slp_response = supabase.table("slp").select("*").eq("slpusername", username).eq("slppassword", password).execute()
    slp_users = slp_response.data

    if slp_users:
        user = slp_users[0]
        user_id = user["slpid"]
        res = RedirectResponse(url="/slp/", status_code=302)
        res.set_cookie(key="user_id", value=str(user_id))
        res.set_cookie(key="role", value="slp")
        return res

    # If not an SLP, check as patient
    patient_response = supabase.table("patients").select("*").eq("pusername", username).eq("ppassword", password).execute()
    patient_users = patient_response.data

    if patient_users:
        user = patient_users[0]
        user_id = user["patientid"]
        res = RedirectResponse(url="/patient/", status_code=302)
        res.set_cookie(key="user_id", value=str(user_id))
        res.set_cookie(key="role", value="patient")
        return res

    return PlainTextResponse("noooo try again", status_code=401)

@app.get("/logout")
async def logout(request: Request):
    res = RedirectResponse(url="/login", status_code=302)
    res.delete_cookie("user_id", path="/")
    res.delete_cookie("role", path="/")
    return res

# @app.get("/create-user")
# def create_user():
#     result = supabase.table("user").insert({"username": "sora", "age": 20}).execute()
#     return result.data

# @app.post("/stt", response_class=HTMLResponse)
# async def stt(request: Request, file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_FOLDER, file.filename)
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     result = model.transcribe(file_location, language="th")
#     text = result["text"]

#     os.remove(file_location)

#     return templates.TemplateResponse("index.html", {"request": request, "transcript": text})


