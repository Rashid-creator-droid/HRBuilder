from fastapi import APIRouter

from .application.routing import router as application_router
from .specialization.routing import router as specialization_router

router = APIRouter(prefix="/v1")
router.include_router(router=application_router)
router.include_router(router=specialization_router)
