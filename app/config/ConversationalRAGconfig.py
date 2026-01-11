import os
from dotenv import load_dotenv
import redis
from pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace,HuggingFaceEndpoint
from langchain_pinecone import PineconeVectorStore
from motor.motor_asyncio import AsyncIOMotorClient
# from langchain_openai import ChatOpenAI 
# from langchain.chat_models import ChatHuggingFace


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MONGO_URL = os.getenv("DATABASE_URL", "mongodb://localhost:27017/")
INDEX_NAME = os.getenv("INDEX_NAME", "langchainvector")
REDIS_URL = os.getenv("REDIS_URL")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")

client = AsyncIOMotorClient(MONGO_URL)
db = client["Database"]

#database setup
def get_db():
    return db

# Redis setup
def get_redis_client():
    if not REDIS_URL:
        raise ValueError("REDIS_URL environment variable not set.")
    return redis.Redis.from_url(REDIS_URL, decode_responses=True)

# Pinecone setup
def get_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    pc = Pinecone(api_key=PINECONE_API_KEY)
    vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
    return vectorstore


# Google API
def get_google_api_key():
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable not set.")
    return GOOGLE_API_KEY

def get_hugginface_api():
    if not HF_TOKEN:
        raise ValueError("HF token environment variable not set.")
    return HF_TOKEN


