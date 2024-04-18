from fastapi import APIRouter, Form, File, UploadFile
# from src.database.generative_ai_db import upload_files, generate_questions
from src.database.generative_ai_db import getResumeText, get_gemini_response, get_question_suggestion


router = APIRouter(
    prefix="/api/generative_ai",
    tags=["generative_ai"],
    responses={404: {"description": "Not found"}},
)



@router.post("/get-questions-suggestions/")
async def get_questions( role: str = Form(...), company: str = Form(...), interviewer: str = Form(...), numberOfQuestions: int = Form(...), resume: UploadFile = File(...),  previous_questions: str = Form(...)):
    text = await getResumeText(resume)
    questions = get_gemini_response(role, company, interviewer, numberOfQuestions, text, previous_questions)
    suggestions = get_question_suggestion(role, company, interviewer, text, questions)
    return {"questions": questions, "suggestions": suggestions}

   



    

