from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import schemas, crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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