from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import schemas

from schemas.user import *
from services.database import get_db
from services.user import UserService
from auth.utils import *
from repositories.user import *

router = APIRouter(tags=["client"])

auth_service = UserService()

http_bearer = HTTPBearer()
repository = UserRepository()

@router.post("/auth/register", response_model=UserAuthReturn)
async def register_client_user(user: UserAuthData, db: AsyncSession = Depends(get_db)) -> UserAuthReturn:
    """
    Регистрация клиента
    """
    return await auth_service.register_user(user, db)


@router.post("/auth/login", response_model=UserAuthReturn)
async def login_client_user(user: UserAuthData, db: AsyncSession = Depends(get_db)) -> UserAuthReturn:
    """
    Ааторизация клиента

    """
    return await auth_service.login_user(user, db)


@router.get("/user", response_model=UserData)
async def get_authorised_user_information(
        user_id: int = Depends(get_current_user_id),
        db: AsyncSession = Depends(get_db)):
    """
    Получение информации о авторизированном пользователе

    Требуется токен
    """
    return await auth_service.get_user_by_id(user_id, db)


@router.post("/lectures", response_model=CreatedLecture)
async def create_lecture(
        lecture: CreateLecture,
        db: AsyncSession = Depends(get_db)):
    lecture = await repository.create_lecture(lecture.title, lecture.content, db)
    return lecture


@router.get("/lectures", response_model=List[CreatedLecture])
async def create_lecture(
        db: AsyncSession = Depends(get_db)):
    lecture = await repository.get_all_lectures(db)
    return lecture