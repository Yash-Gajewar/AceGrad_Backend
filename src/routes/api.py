from fastapi import APIRouter
from src.endpoints import generative_ai_endp

router = APIRouter()
router.include_router(generative_ai_endp.router)





