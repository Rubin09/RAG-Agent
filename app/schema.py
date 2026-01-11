from pydantic import BaseModel, EmailStr
from datetime import date, time

'''
This is to serialize data fetched from mongodb to send in api response here not used as we do not send data stored in mongodb as 
api response
'''
def serializer(chunk: dict) -> dict:
    """Serialize single chunk."""
    return {
        "id": str(chunk["_id"]),
        "chunk_index": chunk["chunk_index"],
        "chunk_strategy": chunk["chunk_strategy"],
        "chunk_filename": chunk["chunk_filename"],
        "created_at": chunk["created_at"].isoformat()
    }

def list_serializer(chunks: list) -> list:
    """Serialize list of chunks."""
    return [serializer(chunk) for chunk in chunks]

from pydantic import BaseModel, EmailStr
from datetime import date, time


class InterviewBookingRequest(BaseModel):
    """Schema for validating incoming booking requests."""
    name: str
    email: EmailStr
    date: date
    time: time