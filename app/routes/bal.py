from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import get_current_user, get_db
from app.models.user import User

router = APIRouter()

@router.get("/bal")
def get_balance(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {
        "balance": current_user.balance,
        "currency": "INR" 
    }

