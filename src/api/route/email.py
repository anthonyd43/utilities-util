from fastapi import APIRouter, HTTPException
from src.common.models.email import Email


router = APIRouter(
    prefix="/email",
    tags=["Emails"],
) 

@router.get("/", response_model=list[Email])
async def get_emails():
    # Placeholder implementation
    return []

@router.get("/{email_id}", response_model=Email)
async def get_email(email_id: str):
    # Placeholder implementation
    return Email(id=email_id, subject="Sample Email")

@router.post("/", response_model=Email)
async def create_email(email: Email):
    # Placeholder implementation
    return email

@router.delete("/{email_id}")
async def delete_email(email_id: str):
    # Placeholder implementation
    return {"detail": "Email deleted"}
