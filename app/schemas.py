from pydantic import BaseModel
from typing import Optional


# Create Enquiry Request
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


class EnquiryHistory(BaseModel):

    id: int
    customer_name: str
    channel: str
    message: str

    status: str
    sop_matched: Optional[str] = None
    suggested_response: Optional[str] = None
    escalation_reason: Optional[str] = None

    class Config:
        from_attributes = True


class FollowUpRequest(BaseModel):
    delay_minutes: int
    message_template: Optional[str] = None


class EscalationRequest(BaseModel):
    reason: str