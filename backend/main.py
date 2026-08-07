from fastapi import FastAPI
from database.mongo import db

app = FastAPI(
    title="Ticket AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Ticket AI Running Successfully"
    }

@app.get("/health")
def health():
    try:
        db.command("ping")
        return {
            "status": "Healthy",
            "database": "Connected"
        }
    except Exception as e:
        return {
            "status": "Failed",
            "error": str(e)
        }