from fastapi import APIRouter, status, Depends
from ..schemas.default import RequestSchema, ResponseSchema
from app.services.example_service import ExampleService
from app.core.utils.logger import Logger

router = APIRouter()


@router.post(
    "/demo",
    response_model=ResponseSchema,
    status_code=status.HTTP_200_OK,
    summary="这是demo summary",
    description="这是demo description"
)
async def create_demo_item(item: RequestSchema):
    """Create a new demo item."""
    Logger.info(f"{item.name}")
    try:
        result = 10
        
        Logger.info(f"{item.name}")
        return ResponseSchema(
            data=result,
        )
    except Exception as e:
        Logger.exception(f"Error occurred: {e}")
        return ResponseSchema(
            code=500,
            msg=f"{e}",
            data={}
        )