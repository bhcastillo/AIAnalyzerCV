from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from src.llm.processor import run_analysis
from src.utils.utils import read_pdf_text

load_dotenv()

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.post("/analyze")
async def analyze(
    cv_file: UploadFile = File(...),
    job_description: str = Form(...),
):
    contents = await cv_file.read()
    cv_text = read_pdf_text(contents)
    json_str = run_analysis(
        cv_text=cv_text,
        job_description=job_description,
    )
    return json_str
