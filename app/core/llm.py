import os
import asyncio
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from app.config import settings


# initialize once at import time
EMBEDDINGS = None
VECTORSTORE = None
QA_CHAIN = None




def init_vectorstore():
  global EMBEDDINGS, VECTORSTORE, QA_CHAIN
  if EMBEDDINGS is None:
      EMBEDDINGS = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)


  # Use local Chroma for Phase1
  VECTORSTORE = Chroma(persist_directory=settings.chroma_persist_dir, embedding_function=EMBEDDINGS)

  llm = OpenAI(temperature=0, openai_api_key=settings.openai_api_key)
  QA_CHAIN = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=VECTORSTORE.as_retriever())




# ensure init on import
try:
  init_vectorstore()
except Exception:
# quiet failure on import (chroma dir might not exist until ingest runs)
   pass




async def answer_query(query: str, user_id: str = "anon") -> str:
# ensure chain initialized
 if QA_CHAIN is None:
   init_vectorstore()
# run blocking chain in thread
 return await asyncio.to_thread(QA_CHAIN.run, query)