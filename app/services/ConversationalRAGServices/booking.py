import datetime
from ...schema import InterviewBookingRequest  
from ...crud.crud import save_booking_to_db  

async def handle_booking(booking_request: InterviewBookingRequest) -> str:
    """
    Create and save booking entry in MongoDB using Pydantic schema.
    
    Args:
        booking_request: Validated booking data via Pydantic schema
    
    Returns:
        Success or error message
    """
    try:
        # Save to MongoDB (already validated by FastAPI)
        booking_result = await save_booking_to_db(booking_request)
        
        # Extract from the validated schema, not from result
        return f"Interview booked successfully for {booking_request.name} on {booking_request.date} at {booking_request.time}."
        
    except Exception as e:
        return f"Failed to book interview: {e}"