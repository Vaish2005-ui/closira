# Closira AI Internship Assignment

AI-powered customer enquiry workflow system built using FastAPI and React Native.

---

# Tech Stack

## Backend
- FastAPI
- Python
- SQLite
- SQLAlchemy
- Pydantic

## Frontend
- React Native
- Expo
- React Navigation

---

# Features

## Backend
- Create customer enquiries
- Async SOP processing using BackgroundTasks
- SOP matching system
- Escalation handling
- Follow-up scheduling
- Enquiry history tracking
- Health check endpoint
- JSON logging

## Frontend
- Dashboard screen
- Leads management screen
- Conversation detail screen
- Escalation screen
- Follow-up screen
- Bottom tab navigation
- CRM-style UI with mock data

---

# API Endpoints

```http
POST /enquiry
GET /enquiry/{id}/history
POST /enquiry/{id}/escalate
POST /enquiry/{id}/follow-up
GET /health
Project Structure
AI_Internship_task/
│
├── app/
│   ├── main.py
│   ├── crud.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── sop_matcher.py
│   ├── logger.py
│   └── routes/
│
├── closira-frontend/
│   ├── App.js
│   └── package.json
│
├── requirements.txt
└── README.md
Backend Setup
pip install -r requirements.txt
uvicorn app.main:app --reload

API Docs:

http://127.0.0.1:8000/docs
Frontend Setup
cd closira-frontend
npm install
npx expo start
Example Payload
{
  "customer_name": "Vaishnavi",
  "channel": "whatsapp",
  "message": "I need pricing details"
}
Future Improvements
AI/NLP intent classification
PostgreSQL integration
Authentication system
Real-time notifications
Backend/frontend integration

Author
##Vaishnavi Falle
