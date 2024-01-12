from db import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Users(db.Model):
    __tablename__ = "users_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

class Item(db.Model):
    __tablename__ = "items_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

class Basket(db.Model):
    __tablename__ = "basket_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users_table.id"))
    item_id = mapped_column(ForeignKey("items_table.id"))
    item = db.relationship(Item, lazy=True)