from fastapi import APIRouter, UploadFile, File,  Form, Request, HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from app.services.convertor import convert_file
from app.services.auth_client import get_user_age

router = APIRouter()

MIN_AGE_FOR_PROFANITY = 16

@router.post("/")
async def convert_endpoint(
    request: Request,
    file: UploadFile = File(...),
    target_format: str = Form(...),
    run_profanity: bool = Form(False),
    run_spellcheck: bool = Form(False)
):
    
    # Only check age if profanity filter was requested
    if run_profanity:
        auth_header = request.headers.get("Authorization")
        age = await get_user_age(auth_header)

        if age < MIN_AGE_FOR_PROFANITY:
            raise HTTPException(
                status_code=403,
                detail=f"Profanity filter is restricted to users aged {MIN_AGE_FOR_PROFANITY}+"
            )
    # endpoint to handle file conversion requests

    # Call conversion function
    output_path = await convert_file(file, target_format, run_profanity, run_spellcheck)

    return JSONResponse(
        {"message": "Conversion endpoint reached.", "output_path": output_path}
    )