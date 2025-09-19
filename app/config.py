from pydantic import BaseSettings


class Settings(BaseSettings):
   openai_api_key: str
   chroma_persist_dir: str = "./chroma_db"
   app_host: str = "0.0.0.0"
   app_port: int = 8000


# Twilio (optional)
   twilio_account_sid: str | None = None
   twilio_auth_token: str | None = None
   twilio_whatsapp_number: str | None = None


# Pinecone placeholders
   pinecone_api_key: str | None = None
   pinecone_env: str | None = None
   pinecone_index: str | None = None


class Config:
  env_file = ".env"


settings = Settings()