# Closira Backend Assignment

AI-powered customer enquiry handling backend built using FastAPI.

---

## Overview

This project simulates Closira’s customer enquiry workflow system.

The backend handles:
- inbound customer enquiries
- SOP matching
- asynchronous processing
- enquiry escalation
- follow-up scheduling
- conversation history tracking

The system is built using FastAPI and SQLite with background task processing.

---

# Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic

---

# Features

## 1. Create Enquiry
Create a new inbound enquiry using:
- customer name
- communication channel
- message

Endpoint:
POST `/enquiry`

---

## 2. Async SOP Processing

After enquiry creation:
- a background task processes the enquiry
- matches message against predefined SOPs
- generates suggested response
- escalates unmatched enquiries

Implemented using:
FastAPI BackgroundTasks

---

## 3. SOP Matching

Hardcoded SOP categories:
- Pricing Enquiry
- Booking Enquiry
- Complaint
- After Hours

Keyword-based matching logic is used.

---

## 4. Escalation Handling

Endpoint:
POST `/enquiry/{id}/escalate`

Allows manual escalation with a reason.

---

## 5. Follow-up Scheduling

Endpoint:
POST `/enquiry/{id}/follow-up`

Allows follow-up scheduling with:
- delay in minutes
- optional message template

---

## 6. Enquiry History

Endpoint:
GET `/enquiry/{id}/history`

Returns:
- enquiry details
- SOP matched
- suggested response
- escalation details
- status

---

## 7. Health Check

Endpoint:
GET `/health`

Checks:
- API availability
- database connectivity

---

# Database Choice

SQLite was chosen because:
- lightweight
- easy local setup
- sufficient for assignment scope
- no external database configuration required

---

# BackgroundTasks vs Celery

FastAPI BackgroundTasks was chosen instead of Celery because:
- simpler setup
- lightweight async processing
- sufficient for assignment requirements
- no distributed task queue needed

Celery would be more suitable for:
- large-scale production systems
- distributed workers
- heavy asynchronous workloads

---

# Project Structure

```text
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── sop_matcher.py
├── logger.py
│
└── routes/
    └── enquiry.py

Installation & Setup
1. Clone Repository
git clone <repository-url>
2. Install Dependencies
pip install -r requirements.txt
3. Run Server
uvicorn app.main:app --reload
4. Open API Docs
http://127.0.0.1:8000/docs
Example API Payloads
Create Enquiry
{
  "customer_name": "Vaishnavi",
  "channel": "whatsapp",
  "message": "I need pricing details"
}
Escalate Enquiry
{
  "reason": "Customer requested human support"
}
Schedule Follow-up
{
  "delay_minutes": 30,
  "message_template": "We will contact you shortly"
}
Logging

Structured JSON logging is implemented for:

enquiry creation
SOP processing
escalation events
Error Handling

The API includes:

validation using Pydantic
meaningful error responses
safe database handling
graceful failure handling
Known Limitations
SOP matching uses simple keyword logic
no authentication system
no production deployment configuration
follow-ups are simulated only
Future Improvements
AI-based NLP intent classification
PostgreSQL integration
Celery + Redis worker queue
Authentication & authorization
Real-time notifications
Multi-tenant support
Author

# Vaishnavi Falle
