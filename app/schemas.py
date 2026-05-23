from pydantic import BaseModel
from typing import Optional


class EnquiryCreate(BaseModel):
    customer_name: str
    channel: str
    message: str


class EnquiryResponse(BaseModel):
    id: int
    customer_name: str
    channel: str
    message: str
    status: str

    class Config:
        from_attributes = True