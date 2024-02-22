from fastapi import APIRouter, File, UploadFile, HTTPException
from typing import List
from src.database.generative_ai_db import upload_files, generate_questions

router = APIRouter(
    prefix="/api/generative_ai",
    tags=["generative_ai"],
    responses={404: {"description": "Not found"}},
)



@router.post("/get-questions")
async def get_questions(query_string, files: List[UploadFile] = File(...)):
    upload_files_response = await upload_files(files)
    print(upload_files_response)
    responseJson = await generate_questions(query_string, upload_files_response["uuid_number"])
    print(responseJson["answer"])
    return responseJson
    

