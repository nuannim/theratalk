from fastapi import FastAPI, Request, Form, Depends
from app.routers import userRoute
from app.routers import docRoute
from fastapi.middleware import Middleware
from app.middleware.auth.auth import AuthMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.db import supabase, get_user
# from db import get_user
from fastapi.responses import HTMLResponse, RedirectResponse, PlainTextResponse

# middleware=[Middleware(AuthMiddleware)]
app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(userRoute.router, prefix="/user")
app.include_router(docRoute.router, prefix="/doc")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("test.html", {
        "request": request
    })

# @app.get("/login")
# async def login(request: Request):
#     return templates.TemplateResponse("login.html", {
#         "request": request
#     })

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

    user = get_user(username, password)
    if user:
        return {"message": f"Login successfully as {username}", "data": user}
    # return templates.TemplateResponse("login.html", {
    #     "request": request,
    #     "error": "Invalid credentials. Try again."
    # })
    return PlainTextResponse("noooo try again", status_code=401)

# @app.post("/login")
# async def login(request: Request):
#     return templates.TemplateResponse("test.html", {
#         "request": request
#     })

@app.get("/create-user")
def create_user():
    result = supabase.table("user").insert({"username": "sora", "age": 20}).execute()
    return result.data

# @app.post("/stt", response_class=HTMLResponse)
# async def stt(request: Request, file: UploadFile = File(...)):
#     file_location = os.path.join(UPLOAD_FOLDER, file.filename)
#     with open(file_location, "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)

#     result = model.transcribe(file_location, language="th")
#     text = result["text"]

#     os.remove(file_location)

#     return templates.TemplateResponse("index.html", {"request": request, "transcript": text})


