from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import whisper
import shutil
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model = whisper.load_model("tiny")
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/stt", response_class=HTMLResponse)
async def stt(request: Request, file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe(file_location, language="th")
    text = result["text"]

    os.remove(file_location)

    return templates.TemplateResponse("index.html", {"request": request, "transcript": text})
