from datetime import datetime
from typing import List, Dict, Any
from ..config.DocumentIngestionconfig import get_db
from bson import ObjectId
from fastapi import HTTPException

from ..schema import InterviewBookingRequest


#for document ingestion
async def insert_chunks_db(metadata_list: List[Dict[str, Any]]) -> List[str]:
    """
    Insert multiple chunk metadata documents at once (MongoDB version).

    Args:
        metadata_list: List of metadata dicts for chunks.

    Returns:
        List of inserted document IDs
    """
    # Get MongoDB collection
    try:
        db = get_db()
        collection = db["chunk_metadata"]
    
        # Ensure created_at is datetime
        for meta in metadata_list:
            if "created_at" in meta and isinstance(meta["created_at"], str):
                meta["created_at"] = datetime.fromisoformat(meta["created_at"].replace('Z', '+00:00'))
    
        # Insert all documents at once - USING AWAIT
        result = await collection.insert_many(metadata_list)  # ← This is async/await!
    
        return [str(id) for id in result.inserted_ids]
    
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail="Failed to insert Chunks"
        )



#for Conversational Rag 
async def save_booking_to_db(booking: InterviewBookingRequest) -> Dict[str, Any]:
    """
    Save interview booking to MongoDB using Pydantic schema.
    
    Args:
        booking: Validated InterviewCreate schema
    
    Returns:
        Complete stored document with MongoDB _id
    
    Raises:
        Exception: If database operation fails
    """
    try:
        collection = get_db()["interviews"]
        
        # Convert Pydantic model to dictionary (includes all fields)
        booking_dict = booking.model_dump()
         
        # Store complete document
        await collection.insert_one(booking_dict)
        
        return booking_dict
        
    except Exception as e:
        raise HTTPException(status_code=400,detail=e)