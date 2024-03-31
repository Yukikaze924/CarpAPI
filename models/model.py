import enum
from pydantic import BaseModel

class UserModel(BaseModel):
    isUserValid: bool
    account: str = None
    nickname: str = None
    password: str = None
    avatar: str = None

class LoginModel(BaseModel):
    account: str
    password: str

class ArticleModel(BaseModel):
    id: int
    date: int
    title: str
    subtitle: str
    category: str
    cover: str
    chapter: str

class Logo(enum.Enum):
    Default=1
    Ukraine=2
    Russia=3
    Rainbow=4