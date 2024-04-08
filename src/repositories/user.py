from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User as UserModel

from models.user import *
from models.user import UserRole


class UserRepository:

    async def create_user(self, email: str, password: bytes, db: AsyncSession, role: str = UserRole.INTERN) -> UserModel:
        user = UserModel(email=email, password=password, role=role)
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
        q = select(Test)
        print(q)
        exec = await db.execute(q)
        test = exec.scalars().first()

        await db.refresh(test)
        await test.questions.load()
        return test
    async def get_questions(self, db: AsyncSession):
        q = select(Question)
        exec = await db.execute(q)
        questions = exec.scalars()
        return questions
