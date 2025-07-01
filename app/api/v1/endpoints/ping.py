from fastapi import APIRouter, status
from ..schemas.default import ResponseSchema

router = APIRouter()

@router.get(
    "/ping",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="ping endpoint",
    description="Ping endpoint"
)
async def ping():
    return ResponseSchema(data="pong")