from fastapi import APIRouter

from .application.routing import router as application_router


router = APIRouter(prefix="/v1")
router.include_router(router=application_router)
