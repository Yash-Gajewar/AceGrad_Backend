from fastapi import APIRouter, File, UploadFile, HTTPException
from src.database.transcript_operations import extract_transcript;

router = APIRouter(
    prefix="/api/transcript",
    tags=["transcript"],
    responses={404: {"description": "Not found"}},
)


@router.get("/extract_text/")
async def get_extracted_text(videoPath: str):
    extracted_text = extract_transcript(videoPath)
    return {"text": extracted_text}


