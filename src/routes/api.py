from fastapi import APIRouter
from src.endpoints import generative_ai_endp
from src.endpoints import transcript_endp

router = APIRouter()
router.include_router(generative_ai_endp.router)
router.include_router(transcript_endp.router)





