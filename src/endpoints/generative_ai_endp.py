from fastapi import APIRouter, Form, File, UploadFile
# from src.database.generative_ai_db import upload_files, generate_questions
from src.database.generative_ai_db import getResumeText, get_gemini_response;


router = APIRouter(
    prefix="/api/generative_ai",
    tags=["generative_ai"],
    responses={404: {"description": "Not found"}},
)



@router.post("/get-questions/")
async def get_questions( role: str = Form(...), company: str = Form(...), interviewer: str = Form(...), numberOfQuestions: int = Form(...), resume: UploadFile = File(...) ):
    text = await getResumeText(resume)
    questions = get_gemini_response(role, company, interviewer, numberOfQuestions, text)
    return questions


   



    

