from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

complaints = []


class ComplaintCreate(BaseModel):
    description: str = Field(min_length=10, max_length=500)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    citizen_phone: str = Field(pattern=r"^[6-9]\d{9}$")


@app.get("/")
def home():
    return {"message": "Hello CivicWitness"}


@app.post("/complaints", status_code=201)
def create_complaint(complaint: ComplaintCreate):
    new_complaint = {
        "id": len(complaints) + 1,
        "status": "RECEIVED",
        **complaint.model_dump(),
    }
    complaints.append(new_complaint)
    return new_complaint