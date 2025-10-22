from typing import Any, Dict

from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: bytes = File(...)
) -> Dict[str, int]:
    """
    Upload a file and return its size in bytes.
    
    This endpoint accepts any file type and returns the file size
    without storing the file on the server.
    """
    # Calculate the size of the uploaded file in bytes
    file_size = len(file)
    
    # Return the file size as a JSON response
    return {"size": file_size}

# Made with Bob