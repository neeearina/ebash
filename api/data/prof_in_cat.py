import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Proff(SqlAlchemyBase):
    __tablename__ = 'professions'

    id_p = sqlalchemy.Column(sqlalchemy.Integer,
                             primary_key=True, autoincrement=True)
    id_category = sqlalchemy.Column(sqlalchemy.Integer, nullable=True, unique=False)
    name = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    zarplata = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)

