from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import get_current_user, get_db
from app.models.product import Product
from app.models.transaction import Transaction
from app.models.user import User

router = APIRouter()

@router.post("/buy")
def buy_product(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    product_id = payload.get("product_id")

    if not isinstance(product_id, int):
        raise HTTPException(status_code=400, detail="Invalid product ID")

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=400, detail="Invalid product")

    if current_user.balance < product.price:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # Deduct balance
    current_user.balance -= product.price

    # Record transaction
    txn = Transaction(
        user_id=current_user.id,
        kind="debit",
        amt=product.price,
        updated_bal=current_user.balance
    )

    db.add(txn)
    db.commit()
    db.refresh(current_user)

    return {
        "message": "Product purchased",
        "balance": current_user.balance
    }
