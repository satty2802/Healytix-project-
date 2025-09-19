from sqlmodel import SQLModel, create_engine, Session
from app.config import settings


DATABASE_URL = f"sqlite:///./dev.db"
engine = create_engine(DATABASE_URL, echo=False)


def init_db():
  SQLModel.metadata.create_all(engine)


def get_session():
  return Session(engine)