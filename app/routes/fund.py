from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import get_current_user, get_db
from app.models.user import User
from app.models.transaction import Transaction

router = APIRouter()

@router.post("/fund")
def fund_account(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    amt = payload.get("amt")

    if not isinstance(amt, int) or amt <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    current_user.balance += amt

    # ✅ Add a credit transaction
    txn = Transaction(
        user_id=current_user.id,
        kind="credit",
        amt=amt,
        updated_bal=current_user.balance
    )

    db.add(txn)
    db.commit()
    db.refresh(current_user)

    return {"balance": current_user.balance}

