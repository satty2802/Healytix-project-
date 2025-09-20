from fastapi import APIRouter, Request
from twilio.twiml.messaging_response import MessagingResponse

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    """
    Twilio will send POST requests here whenever a user sends a WhatsApp message.
    """
    data = await request.form()
    user_message = data.get("Body", "")

    # For now, just echo back
    reply = MessagingResponse()
    reply.message(f"You said: {user_message}")

    return str(reply)
