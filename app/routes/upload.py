from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import os

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    # Save uploaded file as temp file
    _, ext = os.path.splitext(file.filename)
    with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    file_size = os.path.getsize(tmp_path)

    return JSONResponse(
        {"message": "File uploaded successfully.",
         "filename": file.filename, 
         "saved_as": tmp_path, 
         "size": file_size}
    )
