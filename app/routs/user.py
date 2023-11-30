from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from app.config.database import get_session
from app.responses.user_response import UserResponse
from app.schemas.user_schemas import RegisterUser
from app.services.user_service import create_user_account

user_route = APIRouter(
    prefix='/user',
    tags=['Users'],
    responses={404: {"description": "Not found"}}
)


@user_route.post("", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def register_user(data: RegisterUser, session: Session = Depends(get_session)):
    # a = UserResponse(id=12, name=data.name, email=data.email)
    # return a
    return await create_user_account(data, session)
