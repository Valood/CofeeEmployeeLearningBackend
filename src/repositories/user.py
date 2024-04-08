from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from models.user import User as UserModel

from models.user import *
from models.user import UserRole


class UserRepository:

    async def create_user(self, email: str, password: bytes, name: str, city: str,  db: AsyncSession, role: str = UserRole.INTERN) -> UserModel:
        user = UserModel(email=email, password=password, name=name, city=city, role=role)
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def get_user_by_email_or_none(self, email: str, db: AsyncSession) -> UserModel:
        q = select(UserModel).where(UserModel.email == email)
        exec = await db.execute(q)
        user = exec.scalar()
        return user

    async def get_user_by_id_or_none(self, id: int, db: AsyncSession) -> UserModel:
        q = select(UserModel).where(UserModel.id == id)
        exec = await db.execute(q)
        user = exec.scalar()
        return user

    async def create_lecture(self, title: str, content: str,  db: AsyncSession):
        lecture = Lecture(title=title, content=content)
        db.add(lecture)
        await db.commit()
        await db.refresh(lecture)
        return lecture

    async def get_all_lectures(self, db: AsyncSession):
        q = select(Lecture)
        exec = await db.execute(q)
        lectures = exec.scalars()
        return lectures

    async def get_test(self, db: AsyncSession):
        q = select(Test).options(selectinload(Test.questions).selectinload(Question.variant_answers))
        exec = await db.execute(q)
        test = exec.scalars().first()
        return test
    async def get_questions(self, db: AsyncSession):
        q = select(Question)
        exec = await db.execute(q)
        questions = exec.scalars()
        return questions

    async def get_variant_answer_by_id(self, variant_id: int, db: AsyncSession):
        q = select(VariantAnswer).where(VariantAnswer.id == variant_id)
        exec = await db.execute(q)
        variant = exec.scalar()
        return variant

    async def up_rank_of_user(self, id: int,  role: str,  db: AsyncSession):

        match role:
            case UserRole.ADMIN:
                new_role = UserRole.HR

            case UserRole.BARISTA:
                new_role = UserRole.MANAGER

            case UserRole.MANAGER:
                new_role = UserRole.ADMIN

            case UserRole.INTERN:
                new_role = UserRole.BARISTA


        q = select(UserModel).where(UserModel.id == id)
        exec = await db.execute(q)
        user = exec.scalar()
        user.role = new_role
        await db.commit()
        await db.refresh(user)
        return new_role