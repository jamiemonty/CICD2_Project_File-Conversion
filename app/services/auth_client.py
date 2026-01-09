import os
import httpx
from fastapi import HTTPException

AUTH_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")

async def get_user_age(auth_header: str) -> int:
    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    url = f"{AUTH_URL}/api/v1/users/me/age"

    async with httpx.AsyncClient(timeout=5.0) as client:
        r = await client.get(url, headers={"Authorization": auth_header})

    if r.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    if r.status_code != 200:
        raise HTTPException(status_code=502, detail="Auth service error")

    data = r.json()
    age = data.get("age")

    if age is None:
        raise HTTPException(status_code=502, detail="Auth service did not return age")

    return int(age)
