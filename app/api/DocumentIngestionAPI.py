from fastapi import APIRouter, UploadFile, File, Query, HTTPException
from typing import Dict, Any
import logging
from ..services.DocumentIngestionServices.upload import upload_to_mongodb

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    strategy: str = Query("semantic", description="Chunking strategy: semantic or recursive")
) -> Dict[str, Any]:
    """
    Upload and process a document for RAG system.
    """
    # Validate file
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")
    
    if not file.content_type in ["application/pdf", "text/plain"]:
        raise HTTPException(
            status_code=415, 
            detail=f"Unsupported file type: {file.content_type}. Use PDF or TXT."
        )
    
    valid_strategies = ["semantic", "recursive"]
    if strategy not in valid_strategies:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid chunking strategy: {strategy}. Must be one of: {', '.join(valid_strategies)}"
        )
    
    try:
        # Read file
        content_bytes = await file.read()
        
        if len(content_bytes) == 0:
            raise HTTPException(status_code=400, detail="Empty file")
        
        
        
        result = await upload_to_mongodb(
            content_bytes=content_bytes,
            file_type=file.content_type,
            filename=file.filename,
            strategy=strategy
        )
        
        # Success response
        return {
            "status": "success",
            "message": f"Successfully processed {file.filename}",
            "filename": file.filename,
            "file_size": len(content_bytes),
            "strategy": strategy,
            "chunks_created": result.get("chunks_length", 0),
            "top_chunks_preview": result.get("top_chunks", []),
            "chunk_ids": result.get("chunk_ids", [])[:5]  # First 5 IDs
        }
        
    
        
    except Exception as e:
        logger.error(f"Upload failed for {file.filename}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )