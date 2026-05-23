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

class EnquiryHistory(BaseModel):

    id: int
    customer_name: str
    channel: str
    message: str

    status: str
    sop_matched: Optional[str]
    suggested_response: Optional[str]
    escalation_reason: Optional[str]

    class Config:
        from_attributes = True

    class Config:
        from_attributes = True

    