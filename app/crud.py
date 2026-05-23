from sqlalchemy.orm import Session

from . import models, schemas
from .sop_matcher import match_sop
from .logger import logger


# Create Enquiry
def create_enquiry(db: Session, enquiry: schemas.EnquiryCreate):

    db_enquiry = models.Enquiry(
        customer_name=enquiry.customer_name,
        channel=enquiry.channel,
        message=enquiry.message
    )

    db.add(db_enquiry)
    db.commit()
    db.refresh(db_enquiry)

    logger.info(f"Enquiry created: {db_enquiry.id}")

    return db_enquiry


# Process Enquiry in Background
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

    logger.info(f"SOP processed for enquiry: {enquiry.id}")

    db.commit()


# Get Enquiry History
def get_enquiry_history(db: Session, enquiry_id: int):

    return db.query(models.Enquiry).filter(
        models.Enquiry.id == enquiry_id
    ).first()


# Escalate Enquiry
def escalate_enquiry(
    db: Session,
    enquiry_id: int,
    reason: str
):

    enquiry = db.query(models.Enquiry).filter(
        models.Enquiry.id == enquiry_id
    ).first()

    if not enquiry:
        return None

    enquiry.status = "escalated"
    enquiry.escalation_reason = reason

    db.commit()
    db.refresh(enquiry)

    return enquiry


# Schedule Follow-up
def schedule_follow_up(
    db: Session,
    enquiry_id: int,
    delay_minutes: int,
    message_template: str = None
):

    enquiry = db.query(models.Enquiry).filter(
        models.Enquiry.id == enquiry_id
    ).first()

    if not enquiry:
        return None

    enquiry.follow_up_delay = delay_minutes
    enquiry.follow_up_message = message_template
    enquiry.status = "follow-up scheduled"

    db.commit()
    db.refresh(enquiry)

    return enquiry