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
    followers: Mapped[List["Followers"]]= relationship()


class Post(Base):
    __tablename__ = 'post'

    post_id = mapped_column(Integer, primary_key=True)
    post_name =mapped_column(String(50))
    post_footer=mapped_column(String(100))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    comments: Mapped[List[comments]] = relationship(secondary=association_table)
    media_id: Mapped[int] = mapped_column(ForeignKey("media.id"))


class Followers(Base):
    __tablename__ = 'followers'
 
    follower_id = Column(Integer, primary_key=True)
    street_name =mapped_column(String(250))
    street_number = mapped_column(String(250))
    post_code = mapped_column(String(250), nullable=False)  
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

class Comments(Base):
    __tablename__ = 'comments'   

    comment_id = mapped_column(Integer, primary_key=True)
    comment_text =mapped_column(String(50), nullable=False)
    post: Mapped[List["Post"]] = relationship()

    

class Media(Base):
    __tablename__ = 'media'
  
    id = Column(Integer, primary_key=True)
    post: Mapped[List["Post"]] = relationship()
    
class Base(DeclarativeBase):
    pass
association_table = Table (
    "association_table",
    Base.metadata,
    Column("post_id", ForeignKey("post.id"), primary_key=True),
    Column("comments_id", ForeignKey("comments.id"), primary_key=True),
)    
    

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
