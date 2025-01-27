import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, Mapped
from typing import List
from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name=mapped_column(String(50),nullable=False)
    contraseña =mapped_column(String(20), nullable=False)
    email=mapped_column(String(50), nullable=False)
    post: Mapped[List["Post"]] = relationship()
    followers: Mapped[List["Follower"]]= relationship()
    comments : Mapped[List["Comments"]]= relationship()


class Post(Base):
    __tablename__ = 'post'

    post_id = mapped_column(Integer, primary_key=True)
    post_name =mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))
    Comments_id: Mapped[int] = mapped_column(ForeignKey("comments.id"))


class Follower(Base):
    __tablename__ = 'followers'
    user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

class Comments(Base):
    __tablename__ = 'comments'
    comment_id = mapped_column(Integer, primary_key=True)
    comment_text =mapped_column(String(50), nullable=False)
    post: Mapped[List["Post"]] = relationship()
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    

    

class Media(Base):
    __tablename__ = 'media'
  
    id = Column(Integer, primary_key=True)
    post: Mapped[List["Post"]] = relationship()

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
