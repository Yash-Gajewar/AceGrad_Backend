from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
# from src.database.generative_ai_db import upload_files, generate_questions
from src.database.generative_ai_db import getResumeText;
import google.generativeai as genai


router = APIRouter(
    prefix="/api/generative_ai",
    tags=["generative_ai"],
    responses={404: {"description": "Not found"}},
)

genai.configure(api_key="AIzaSyCcNEqSQHwga67N96nU3EV6AFiDCySQxas")


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response =chat.send_message(question,stream=True)
#     return response

def get_gemini_response(role, company, interviewer, numberOfQuestions, text):
    result = ""
    query = f"You are an interviewer of type {interviewer}, of  Company: {company}, taking an interview of a candidate applying for Role: {role}. The following is the Resume of the candidate: {text}. Generate {numberOfQuestions} questions one after the other only with question number and question itself with no other data that could potentially be asked to the candidate based on his resume, skills, experience, latest trends, data structes and algorithms and company motives and company related technologies."
    response = chat.send_message(query,stream=True)
    for chunk in response:
        result += (chunk.text)
    
    questions = result.split('\n')
    questions = [question.strip() for question in questions if question.strip()]

    return questions


@router.post("/get-questions")
async def get_questions(role : str, company : str, interviewer : str, numberOfQuestions: str, resume: UploadFile = File(...)):
    text = await getResumeText(resume)
    questions = get_gemini_response(role, company, interviewer, numberOfQuestions, text)
    return questions

   



    

