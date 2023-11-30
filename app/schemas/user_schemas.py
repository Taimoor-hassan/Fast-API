from pydantic import EmailStr, BaseModel


class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    password: str
