from fastapi import APIRouter, Request, Form
from pydantic import BaseModel
from app.core.llm import answer_query


router = APIRouter()


class IncomingMessage(BaseModel):
   text: str
   from_id: str | None = None


@router.post("/message")
async def receive_message(payload: IncomingMessage):
# This endpoint accepts JSON payloads for local testing
  reply = await answer_query(payload.text, payload.from_id or "anon")
  return {"reply": reply}


# Twilio sends form-encoded data. Example handler for Twilio SMS/WhatsApp sandbox
@router.post("/twilio", response_model=dict)
async def twilio_webhook(Body: str = Form(...), From: str = Form(...)):
# Body is incoming text, From is sender (eg whatsapp:+91...)
  reply = await answer_query(Body, From)
# Twilio wants TwiML or a simple response; we'll return JSON for now
  return {"reply": reply}