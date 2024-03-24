import enum
from pydantic import BaseModel

class UserModel(BaseModel):
    isUserValid: bool
    account: str = None
    nickname: str = None
    password: str = None

class LoginModel(BaseModel):
    account: str
    password: str

class Logo(enum.Enum):
    Default=1
    Ukraine=2
    Russia=3
    Rainbow=4