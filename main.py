from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS so RapidAPI test tools work
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...)):
    return {"filename": file.filename, "summary": "This is a test summary."}
from fastapi import FastAPI, UploadFile, File, Form
from summarizer import summarize_text
from utils import extract_text_from_pdf

app = FastAPI()

@app.post("/summarize/")
async def summarize(
    file: UploadFile = File(...),
    mode: str = Form("medium")
):
    contents = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(contents)

    text = extract_text_from_pdf("temp.pdf")
    result = summarize_text(text, mode)
    return result
