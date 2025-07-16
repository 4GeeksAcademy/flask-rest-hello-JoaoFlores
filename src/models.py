from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


db = SQLAlchemy()


class User(db.Model):

     __tablename__ = "User"

     id: Mapped[int] = mapped_column(primary_key=True)
     username: Mapped[str] =mapped_column(String(120),nullable= False)
     firstname: Mapped[str] = mapped_column(String(120), nullable=False)
     lastname: Mapped[str] = mapped_column(String(120), nullable=False)
     email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
     password: Mapped[str] = mapped_column(nullable=False)
     is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

     follower: Mapped[list["Follower"]] = relationship(back_populates="author")

     def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "firstname" : self.firstname,
            "lastname" : self.lastname
            # do not serialize the password, its a security breach
        }
    


class Follower(db.Model):
    __tablename__ = "Follower"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_from_id : Mapped[int] = mapped_column(ForeignKey("User.id"))
    user_to_id : Mapped["int"] = mapped_column(ForeignKey( "User.id"))
    author: Mapped["User"] = relationship(back_populates="follower")

class Post (db.Model):
    __tablename__ = "Post"
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id : Mapped[int] = mapped_column(ForeignKey("User.id"))
    comments: Mapped[list["Comment"]] = relationship(back_populates="author")
    media: Mapped["Media"] = relationship(back_populates="post_media")
    

    def serialize(self):
        return{
            "id": self.id
        }

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120), nullable= False)

    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    author : Mapped["Post"] = relationship(back_populates="comments")
    

class Media (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(120),nullable=False)
    url: Mapped[str] = mapped_column(String(120),nullable=False)

    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))
    post_media:  Mapped["Post"] = relationship(back_populates="media")