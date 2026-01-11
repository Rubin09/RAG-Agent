# Conversational RAG & Document Ingestion API

A robust FastAPI-based system that provides intelligent document processing and conversational AI capabilities with built-in interview booking functionality.

## Overview

This project implements a dual-purpose API system:

1. **Document Ingestion API** – Process and vectorize documents for semantic search
2. **Conversational RAG API** – Enable intelligent, context-aware conversations with document retrieval and booking capabilities

---

## Features

### Document Ingestion API

- **Multi-format Support**: Upload and process `.pdf` or `.txt` files
- **Intelligent Chunking**: Choose between two advanced chunking strategies:
  - Recursive Character Chunking
  - LLM Semantic Chunking
- **Vector Storage**: Generate embeddings and store in Pinecone vector database
- **Metadata Management**: Save comprehensive metadata in Database (MongoDB)

### Conversational RAG API

- **Custom RAG Pipeline**: Built without RetrievalQAChain for greater control and flexibility
- **Multi-turn Conversations**: Maintain context across conversation turns with Redis-based memory
- **Intelligent Retrieval**: Context-aware document retrieval from vector database
- **Interview Booking Support**: Integrated booking functionality
- **Agent-based Responses**: Smart response generation

---

---

## API Endpoints

### Document Ingestion API

- `POST /upload` – Upload and process documents

### Conversational RAG API

- `POST /agent` – Initiate or continue conversation with chatbot

---

## Tech Stack

- **Backend Framework**: FastAPI
- **Vector Database**: Pinecone
- **Memory Store**: Redis
- **Database**: MongoDb
- **Python Libraries**:
  - LangChain – LLM orchestration
  - Pydantic – Data validation
  - PyPDF2 – PDF processing
  - Motor – Database
  - python-dotenv – Environment management
  - requests – HTTP client, etc.

---

## Installation & Setup

### Prerequisites

- Python
- MongoDB Compass or Atlas
- Redis
- Pinecone account
- OpenAI API key (or alternative LLM provider In This project Hugging Face token is used)

## Demonstration of Working Endpoints

### Document Ingestion API

- **Upload .pdf or .txt files**
  ![Upload Files](screenshots/DocumentIngestionAPI.png)
- **Extract text and apply any of the two chunking strategies:**

  - Recursive Character Chunking
  - LLM Semantic Chunking  
    ![Text Chunking](screenshots/DocumentIngestionAPIResponse.png)

- **Generate embeddings and store in Pinecone vector database**

  ![Embeddings](<screenshots/VectorDB(Pinecone).png>)

- **Save metadata in MongoDB**

  ![PostgreSQL](screenshots/ChunkMetaDatainMongoDB.png)

### Conversational RAG API

- **Custom RAG pipeline (no RetrievalQAChain)**

  ![RAG Pipeline](screenshots/ConversationalRAGAPI.png)

  ![AGENT-RESPONSE](screenshots/ConversationalRAGAPIResponse.png)

- **Handles multi-turn queries with chat memory stored in Redis**

  ![Chat Memory](screenshots/RedisDB.png)

- **Supports interview booking (name, email, date, time)**

  ![Booking](screenshots/booking1.png)

  ![Booking](screenshots/booking2.png)

  ![Booking](screenshots/booking3.png)

  ![Booking](screenshots/booking4.png)

  ![Booking](screenshots/booking5.png)

---
