from fastapi import APIRouter, Depends
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


@router.post("/enquiry", response_model=schemas.EnquiryResponse)
def create_new_enquiry(
    enquiry: schemas.EnquiryCreate,
    db: Session = Depends(get_db)
):
    return crud.create_enquiry(db, enquiry)