from typing import Any, Dict

from fastapi import APIRouter, File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/upload")
async def upload_file(
    # Use File(...) to indicate this is a required file upload parameter
    # The file content will be read as bytes
    file: bytes = File(...),
) -> Dict[str, int]:
    """
    Upload a file and return its size in bytes.
    
    This endpoint accepts any file type and calculates its size.
    It doesn't store the file permanently, just processes it in memory.
    
    Args:
        file: The uploaded file content as bytes
        
    Returns:
        A JSON object containing the size of the file in bytes
    """
    # Calculate the size of the uploaded file in bytes
    file_size = len(file)
    
    # Return a JSON response with the file size
    # This follows the requirement to return {"size": len(file)}
    return {"size": file_size}

# Made with Bob