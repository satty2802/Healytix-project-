from fastapi import FastAPI
from routes.chat import router as chat_router

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Health Chatbot running on Render!"}

app.include_router(chat_router, prefix="/api")
