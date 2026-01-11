from pydantic import BaseModel
from datetime import datetime

# These models are used only if an endpoint to access the meta data are made (currently not used only used for testing)
# Request Model 
class ChunkMetaDataRequest(BaseModel):
    chunk_index: int
    chunk_strategy: str
    chunk_filename: str


# Response Model 
class ChunkMetaDataResponse(BaseModel):
    chunk_index: int
    chunk_strategy: str
    chunk_filename: str
    created_at: datetime