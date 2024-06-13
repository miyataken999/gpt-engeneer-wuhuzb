from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    profile: str
    team_id: int
    tags: str

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int