"""API version 1 routes."""

from fastapi import APIRouter
from app.api.v1.endpoints import demo, ping

router = APIRouter()
router.include_router(demo.router, tags=["test"])
router.include_router(ping.router, tags=["ping"])