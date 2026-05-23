from fastapi import FastAPI

from .database import Base, engine
from .routes import enquiry

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Closira Backend API",
    description="AI-powered enquiry handling backend",
    version="1.0"
)

app.include_router(enquiry.router)


@app.get("/")
def root():
    return {"message": "Closira API Running"}

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "database": "connected"
    }