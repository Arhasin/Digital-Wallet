from app.core.db import Base, engine
from app.models.user import User
from app.models.transaction import Transaction  
from app.models.product import Product 

# Create all tables
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done!")
