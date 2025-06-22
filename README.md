A simple wallet backend built with FastAPI and SQLAlchemy.

FEATURES:
✅ User registration with password hashing
✅ Basic Authentication for protected endpoints
✅ Fund account (deposit money)
✅ Pay another user
✅ Check your balance
✅ See your transaction history
✅ Add products to a global catalog
✅ Buy products using wallet balance

1. Register User
Create a new user account.
Endpoint: POST /register
Authentication: ❌ No auth required
--Request Body:

{
  "username": "ashu",
  "password": "hunter2"
}
--Response:
Status: 201 Created if successful.

2. Fund Account
Deposit money into the logged-in user's wallet.
Endpoint: POST /fund
Authentication: ✅ Required
--Request Body:
{
  "amt": 10000
}
--Success Response:
{
  "balance": 10000
}

3. Pay Another User
Transfer money from the logged-in user to another user.
Endpoint: POST /pay
Authentication: ✅ Required
--Request Body:
{
  "to": "priya",
  "amt": 100
}
--Success Response:
{
  "balance": 9900
}
Failure Response:
Status: 400 Bad Request
Reason: insufficient funds or recipient doesn’t exist.

4. Check Balance
Endpoint: GET /bal?currency=USD
Authentication: ✅ Required
--Success Response:
{
  "balance": 120.35,
  "currency": "USD"
}

5. View Transaction History
Return a list of all the user’s transactions in reverse chronological order.
Endpoint: GET /stmt
Authentication: ✅ Required
--Response:
[
  { "kind": "debit", "amt": 100, "updated_bal": 9900, "timestamp": "2025-06-09T10:00:00Z" },
  { "kind": "credit", "amt": 10000, "updated_bal": 10000, "timestamp": "2025-06-09T09:00:00Z" }
]

6. Add Product
Admins or logged-in users can add products to a global catalog. Each product includes name, price (in INR), and a short description.
Endpoint: POST /product
Authentication: ✅ Required
--Request Body:
{
  "name": "Wireless Mouse",
  "price": 599,
  "description": "2.4 GHz wireless mouse with USB receiver"
}
--Response:
Status: 201 Created
{
  "id": 1,
  "message": "Product added"
}

7. List All Products
List all available products in the catalog.
Endpoint: GET /product
Authentication: ❌ Not required
--Response:
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "price": 599,
    "description": "2.4 GHz wireless mouse with USB receiver"
  }
]

8. Buy a Product
Use wallet balance to purchase a product. The price should be deducted from the user’s balance and a transaction should be recorded.
Endpoint: POST /buy
Authentication: ✅ Required
--Request Body:
{
  "product_id": 1
}
--Success Response:
{
  "message": "Product purchased",
  "balance": 9301
}
Failure Response: Status: 400 Bad Request

{
  "error": "Insufficient balance or invalid product"
}

Now to run command on your system:
RUN COMMAND:
uvicorn main:app --reload
