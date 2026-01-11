from fastapi import HTTPException
from typing import Any, Dict

from .text_extraction import extract_text
from .chunking import get_text_chunks
from .build_metadata import build_metadata

# MongoDB functions (you need to create these)
from ...crud.crud import insert_chunks_db
from .vectorstorage import store_embeddings  # Keep this if it's already async
from ...config.DocumentIngestionconfig import get_embeddings

async def upload_to_mongodb(
    content_bytes: bytes,
    file_type: str,
    filename: str,
    strategy: str
) -> Dict[str, Any]:
    """
    Process a file: extract text, chunk it, store embeddings, and save metadata to MongoDB.

    Args:
        content_bytes: Raw file content.
        file_type: MIME type of the file ('text/plain' or 'application/pdf').
        filename: Name of the uploaded file.
        strategy: Chunking strategy ('recursive' or 'semantic').

    Returns:
        Dictionary containing the total number of chunks and the first few chunk previews.

    Raises:
        HTTPException: If no chunks are produced from the file.
    """
    try:
        # 1. Extract text from file
        content = extract_text(file_type, content_bytes)
        
        # 2. Get embeddings model
        embeddings = get_embeddings()
        
        # 3. Create chunks (make sure get_text_chunks is async if possible)
        docs_to_index, stats = get_text_chunks(strategy, filename, content, embeddings)
        
        if not docs_to_index:
            raise HTTPException(
                status_code=400, 
                detail="No chunks produced from the file."
            )
        
        store_embeddings(docs_to_index)
        
        metadata_list = build_metadata(docs_to_index, filename)
        
        chunk_ids = await insert_chunks_db(metadata_list)
        
        top_chunks_response = []
        
        for i, doc in enumerate(docs_to_index[:5]):
            top_chunks_response.append({
                "chunk_id": i,
                "chunk_text": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
            })
        
        return {
            "status": "success",
            "filename": filename,
            "chunks_created": len(docs_to_index),
            "chunk_ids": chunk_ids[:10],  
            "chunking_statistics": stats,
            "top_chunks": top_chunks_response,
            "strategy": strategy
        }
        
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process document: {str(e)}"
        )