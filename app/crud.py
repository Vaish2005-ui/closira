from sqlalchemy.orm import Session
from . import models, schemas
from .sop_matcher import match_sop

def create_enquiry(db: Session, enquiry: schemas.EnquiryCreate):
    def process_enquiry(db: Session, enquiry_id: int):

    enquiry = db.query(models.Enquiry).filter(
        models.Enquiry.id == enquiry_id
    ).first()

    if not enquiry:
        return

    result = match_sop(enquiry.message)

    if result:
        enquiry.sop_matched = result["sop"]
        enquiry.suggested_response = result["response"]
        enquiry.status = "qualified"

    else:
        enquiry.status = "escalated"
        enquiry.escalation_reason = "No SOP matched"

    db.commit()

    db_enquiry = models.Enquiry(
        customer_name=enquiry.customer_name,
        channel=enquiry.channel,
        message=enquiry.message
    )

    db.add(db_enquiry)
    db.commit()
    db.refresh(db_enquiry)

    return db_enquiry