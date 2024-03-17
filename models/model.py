from pydantic import BaseModel

class UserModel(BaseModel):
    isUserValid: bool
    account: str = None
    nickname: str = None
    password: str = None

class LoginModel(BaseModel):
    account: str
    password: str