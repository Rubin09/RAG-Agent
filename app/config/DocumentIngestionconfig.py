import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings 

load_dotenv()
MONGO_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017/")
INDEX_NAME = os.getenv("INDEX_NAME", "langchainvector")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

client = AsyncIOMotorClient(MONGO_URL)
db = client["Database"]

def get_db():
    return db

def get_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings

def get_index_name():
    if not INDEX_NAME:
        raise ValueError("INDEX NAME environment variable not set.")
    return  INDEX_NAME

# Pinecone setup
def get_pineconeClient():
    if not PINECONE_API_KEY:
        raise ValueError("PINECONE API KEY environment variable not set.")
    pc = Pinecone(api_key=PINECONE_API_KEY)
    return pc


