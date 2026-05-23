from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Enquiry
@router.post("/enquiry", response_model=schemas.EnquiryResponse)
def create_new_enquiry(
    enquiry: schemas.EnquiryCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    created_enquiry = crud.create_enquiry(db, enquiry)

    background_tasks.add_task(
        crud.process_enquiry,
        db,
        created_enquiry.id
    )

    return created_enquiry


# Get Enquiry History
@router.get(
    "/enquiry/{enquiry_id}/history",
    response_model=schemas.EnquiryHistory
)
def get_history(
    enquiry_id: int,
    db: Session = Depends(get_db)
):

    enquiry = crud.get_enquiry_history(db, enquiry_id)

    if not enquiry:
        return {"error": "Enquiry not found"}

    return enquiry


# Escalate Enquiry
@router.post("/enquiry/{enquiry_id}/escalate")
def escalate_enquiry(
    enquiry_id: int,
    escalation: schemas.EscalationRequest,
    db: Session = Depends(get_db)
):

    enquiry = crud.escalate_enquiry(
        db,
        enquiry_id,
        escalation.reason
    )

    if not enquiry:
        return {"error": "Enquiry not found"}

    return {
        "message": "Enquiry escalated successfully",
        "status": enquiry.status
    }


# Schedule Follow-up
@router.post("/enquiry/{enquiry_id}/follow-up")
def follow_up_enquiry(
    enquiry_id: int,
    follow_up: schemas.FollowUpRequest,
    db: Session = Depends(get_db)
):

    enquiry = crud.schedule_follow_up(
        db,
        enquiry_id,
        follow_up.delay_minutes,
        follow_up.message_template
    )

    if not enquiry:
        return {"error": "Enquiry not found"}

    return {
        "message": "Follow-up scheduled successfully",
        "status": enquiry.status
    }