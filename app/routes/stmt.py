from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.auth import get_current_user, get_db
from app.models.transaction import Transaction

router = APIRouter()

@router.get("/stmt")
def get_statement(current_user = Depends(get_current_user), db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.user_id == current_user.id).order_by(Transaction.timestamp.desc()).all()

    return [
        {
            "kind": txn.kind,
            "amt": txn.amt,
            "updated_bal": txn.updated_bal,
            "timestamp": txn.timestamp.isoformat()
        }
        for txn in transactions
    ]
