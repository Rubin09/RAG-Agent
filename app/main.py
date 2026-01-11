from fastapi import FastAPI 
from .api.DocumentIngestionAPI import router as document_router 
from .api.ConversationalRAGAPI import router as agent_router

app = FastAPI(title = "Converstational RAG API")

app.include_router(document_router)
app.include_router(agent_router)

