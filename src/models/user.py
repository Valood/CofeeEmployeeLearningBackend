from uuid import uuid4
from enum import Enum
import uuid as uuid_pkg

import sqlalchemy
from sqlalchemy import Column, String, select, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID, BYTEA
from sqlalchemy.orm import relationship
from fastapi_restful.guid_type import GUID
from sqlalchemy.sql import func
from sqlalchemy.types import LargeBinary

from services.database import Base


class UserRole:
    INTERN = "intern"
    BARISTA = "barista"
    MANAGER = "manager"
    ADMIN = "admin"
    HR = "hr"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    city = Column(String, nullable=True)
    role = Column(String, default="client")
    email = Column(String, unique=True)
    password = Column(BYTEA, nullable=True)


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    content = Column(String, nullable=True)


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    description = Column(String, nullable=True)
    questions = relationship("Question", back_populates="test", uselist=True)

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=True)
    test = relationship("Test", back_populates="questions")
    test_id = Column(Integer, ForeignKey("tests.id"))
    variant_answers = relationship("VariantAnswer", back_populates="question", uselist=True)


class VariantAnswer(Base):
    __tablename__ = "variant_answers"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, nullable=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="variant_answers")
    is_true = Column(Boolean, default=False)




