from fastapi import APIRouter, Form
from src.database.transcript_operations import process_transcript

router = APIRouter(
    prefix="/api/transcript",
    tags=["transcript"],
    responses={404: {"description": "Not found"}},
)


@router.post("/process_transcript/")
async def get_processed_transcript(transcript: str = Form(...)):
    processed_transcript = process_transcript(transcript)
    return processed_transcript

