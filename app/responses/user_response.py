from pydantic import EmailStr

from app.responses.base_response import BseResponse


class UserResponse(BseResponse):
    id: int
    name: str
    email: EmailStr
    # created_at:
