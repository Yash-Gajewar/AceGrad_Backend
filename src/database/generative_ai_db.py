from fastapi import File, UploadFile, HTTPException
from typing import List
import requests


async def upload_files(files: List[UploadFile] = File(...)):
    for file in files:
        files_data = {'files': (file.filename, file.file, file.content_type)}
        response = requests.post('https://api.jugalbandi.ai/upload-files', files=files_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=response.status_code, detail="File upload failed")
    return "SUCCESS"



async def generate_questions(query_string: str, uuid_number: str):
    url = f"https://api.jugalbandi.ai/query-with-langchain-gpt4?query_string={query_string}&uuid_number={uuid_number}"
    response = requests.get(url)
    if response.status_code == 200:
        responseJson = response.json()
        return responseJson
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch response from the external API")