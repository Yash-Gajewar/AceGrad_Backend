from fastapi import File, UploadFile, HTTPException
from pypdf import PdfReader 
import google.generativeai as genai

# async def upload_files(files: List[UploadFile] = File(...)):
#     for file in files:
#         files_data = {'files': (file.filename, file.file, file.content_type)}
#         response = requests.post('https://api.jugalbandi.ai/upload-files', files=files_data)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise HTTPException(status_code=response.status_code, detail="File upload failed")
#     return "SUCCESS"



# async def generate_questions(query_string: str, uuid_number: str):
#     url = f"https://api.jugalbandi.ai/query-with-langchain-gpt4?query_string={query_string}&uuid_number={uuid_number}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         responseJson = response.json()
#         return responseJson
#     else:
#         raise HTTPException(status_code=response.status_code, detail="Failed to fetch response from the external API")


async def getResumeText(file: UploadFile = File(...)):
    reader = PdfReader(file.file) 
    page = reader.pages[0] 
    text = page.extract_text() 
    return text


genai.configure(api_key="AIzaSyCcNEqSQHwga67N96nU3EV6AFiDCySQxas")


model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# def get_gemini_response(question):
#     response =chat.send_message(question,stream=True)
#     return response

def get_gemini_response(role : str, company : str, interviewer : str, numberOfQuestions : int, text : str, previous_questions : str):
    result = ""
    query = f"You are an interviewer of type {interviewer}, of  Company: {company}, taking an interview of a candidate applying for Role: {role}. The following is the Resume of the candidate: {text}. Generate {numberOfQuestions} questions each one after the other with no other data like question number of '*' symbol,  that could potentially be asked to the candidate based on his resume, skills, experience, latest trends, data structures and algorithms, type of interviewer and company motives and company related technologies."
    response = chat.send_message(query,stream=True)
    for chunk in response:
        result += (chunk.text)

    questions = result.split('\n')
    questions = [question.strip() for question in questions if question.strip()]

    previous_questions = previous_questions.split('\n')
    previous_questions = [question.strip() for question in previous_questions if question.strip()]

    finalQuestions = []

    finalQuestions.extend(previous_questions)
    finalQuestions.extend(questions)
         
    return finalQuestions


def get_question_suggestion(role, company, interviewer, text, questions):
    result = ""
    for question in questions:
            query = f"You are an interviewer of type {interviewer}, of  Company: {company}, taking an interview of a candidate applying for Role: {role}. The following is the {question} for the candidate. The follwoing is the resume of the candidate: {text}. Generate only suggestion on how a candidate should answer such question in an interview effectively in a single paragraph of 3-4 lines no other data like question number of '*' symbol. Note the suggestion should be personalized based on the resume of the cadidate."
            response = chat.send_message(query,stream=True)
            for chunk in response:
                result += (chunk.text)

            result += '\$'

    suggestions = result.split('\$')
    suggestions = [suggestion.strip() for suggestion in suggestions if suggestion.strip()]
    return suggestions

