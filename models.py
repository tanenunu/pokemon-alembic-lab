# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    region = Column(String(100))