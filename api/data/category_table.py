import sqlalchemy
from .db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    __tablename__ = 'category_prof'

    id_c = sqlalchemy.Column(sqlalchemy.Integer,
                             primary_key=True, autoincrement=True)
    name_c = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def __repr__(self):
        return f'{self.name_c}'