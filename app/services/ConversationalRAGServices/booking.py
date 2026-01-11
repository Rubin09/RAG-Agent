from datetime import datetime
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
        
        # date_str = str(booking_request.date)
        # time_str = str(booking_request.time)
        
        
        # booking_dict = {
        #     "name": booking_request.name,
        #     "email": booking_request.email,
        #     "date": date_str,  
        #     "time": time_str,  
        #     "created_at": datetime.now(),
        #     "status": "confirmed"
        # }
        booking_result = await save_booking_to_db(booking_request)
        
        # Extract from the validated schema, not from result
        return f"Interview booked successfully for {booking_request.name} on {booking_request.date} at {booking_request.time}. Booking ID: {booking_result}"
        
    except Exception as e:
        return f"Failed to book interview: {e}"