""" What this file will do:
Accept: Resume (PDF)
Job description
---
Return:
Skills
ATS score
Similarity
Job role
AI suggestions"""

from fastapi import FastAPI, UploadFile, File
import shutil
import os

from Utils.parser import extract_text_from_pdf
from Utils.skills import extract_skills, match_job_roles
from Utils.similarity import calculate_similarity
from Utils.ats import calculate_ats_score, suggest_job_role
from Utils.generate_suggestions import generate_ai_suggestions_llm

app = FastAPI()


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API is running"}


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...), job_desc: str = "Looking for Python, machine learning, pandas, numpy, and data analysis skills."):
    
    # save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # extract text
    resume_text = extract_text_from_pdf(file_path)
    
    # skills
    skills = extract_skills(resume_text)
    
    # similarity
    similarity_score = calculate_similarity(resume_text, job_desc)
    
    # ATS
    ats_result = calculate_ats_score(resume_text, job_desc)
    
    # role suggestion
    best_role, role_scores = suggest_job_role(resume_text)
    
    # AI suggestions
    ai_suggestions = generate_ai_suggestions_llm(
        resume_text,
        job_desc,
        ats_result["missing_skills"]
    )
    
    return {
        "skills": skills,
        "similarity_score": similarity_score,
        "ats": ats_result,
        "best_role": best_role,
        "role_scores": role_scores,
        "ai_suggestions": ai_suggestions
    }