import os
from pathlib import Path
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from app.config import settings


DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "faqs"




def load_documents():
  docs = []
  for md in DATA_DIR.glob("*.md"):
     loader = TextLoader(str(md), encoding="utf-8")
     docs.extend(loader.load())
  return docs




def run():
    print("Loading documents...")
    docs = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.split_documents(docs)


    emb = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)
    persist_dir = settings.chroma_persist_dir
    os.makedirs(persist_dir, exist_ok=True)


    print(f"Creating Chroma vectorstore at {persist_dir}...")
    vectordb = Chroma.from_documents(documents=docs, embedding=emb, persist_directory=persist_dir)
    vectordb.persist()
    print("Ingest finished.")




if __name__ == "__main__":
run()