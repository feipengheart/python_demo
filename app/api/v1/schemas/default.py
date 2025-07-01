from pydantic import BaseModel
from typing import Any

class RequestSchema(BaseModel):
    """
    Demo请求数据模型
    
    示例:
    {
        "name": "Demo Item",
        "description": "A sample demo item"
    }
    """
    name: str
    description: str=""

class ResponseSchema(BaseModel):
    "desc"

    code: int = 200
    data: Any
    msg: str="success"