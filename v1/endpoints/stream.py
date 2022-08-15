from fastapi import APIRouter, status


router = APIRouter(tags=["stream"], prefix="/stream")


@router.get("/video/{video_id}")
async def stream():
    pass
