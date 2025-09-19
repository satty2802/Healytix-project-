from sqlmodel import SQLModel, Field
from datetime import datetime


class Message(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  user_id: str
  text: str
  reply: str | None = None
  created_at: datetime = Field(default_factory=datetime.utcnow)