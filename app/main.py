from fastapi import FastAPI, Depends
from app.routes import auth
from app.core.auth import get_current_user
from app.models.user import User
from app.routes import fund
from app.routes import pay
from app.routes import stmt
from app.routes import product
from app.routes import buy
from app.routes import bal
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))



app = FastAPI()
app.include_router(auth.router)
app.include_router(fund.router)
app.include_router(pay.router)
app.include_router(bal.router)
app.include_router(stmt.router)
app.include_router(product.router)
app.include_router(buy.router)


@app.get("/")
def home():
    return {"message": "Wallet API is running 🚀"}

@app.get("/protected")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello, {current_user.username}! You're authenticated."}
