from typing import List

from pydantic import BaseModel, EmailStr, ConfigDict


class UserAuthReturn(BaseModel):
    model_config = ConfigDict(strict=True)

    email: EmailStr
    id: int
    token: str


class UserAuthData(BaseModel):
    email: EmailStr
    password: str

class RegisterUserSchema(BaseModel):
    email: EmailStr
    password: str
    role: str

class UserData(BaseModel):
    email: EmailStr
    role: str
    id: int

class NewUserReturn(BaseModel):
    id: int
    email: EmailStr
    role: str
    password: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr


class CreatedLecture(BaseModel):
    id: int
    title: str
    content: str

class CreateLecture(BaseModel):
    title: str
    content: str

# class VariantAnswer(BaseModel):

# class Question:
#     question: str
#     answer: List[]