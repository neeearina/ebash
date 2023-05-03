import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class SingUp(SqlAlchemyBase):
    __tablename__ = 'passwords'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    old = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
