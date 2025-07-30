from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel, EmailStr
import time

app = FastAPI()

# Simple in-memory user store (for demo)
users_db = {}

class UserRegistration(BaseModel):
    username: str
    email: EmailStr
    password: str

def send_welcome_email(email: str, username: str):
    """Simulate sending a welcome email (could be replaced with real email logic)."""
    # Simulate some processing time (e.g., sending email)
    print(f"Sending welcome email to {email} for user {username}")
    time.sleep(2)  # Simulate delay
    print(f"Welcome email sent to {email}")

@app.post("/register", status_code=201)
def register_user(user: UserRegistration, background_tasks: BackgroundTasks):
    # Check if user or email is already registered
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already taken.")
    if any(u['email'] == user.email for u in users_db.values()):
        raise HTTPException(status_code=400, detail="Email already registered.")
    
    # Save user to the in-memory database
    users_db[user.username] = {
        "email": user.email,
        "password": user.password  # (hashed in a real app)
    }
    
    # Schedule the email to be sent in the background
    background_tasks.add_task(send_welcome_email, user.email, user.username)
    
    return {"message": "User registered successfully"}
