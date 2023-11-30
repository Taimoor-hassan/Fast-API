from app.models.user import User
from app.services.base_service import session_acr


async def create_user_account(data, session):
    user = User(
        name=data.name,
        email=data.email,
        password=data.password
    )
    session_acr(user, session)
    return user
