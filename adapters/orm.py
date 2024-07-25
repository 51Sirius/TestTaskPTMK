from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship

from domain import model


metadata = MetaData()

employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("midle_name", String(255)),
    Column("birthday", Date),
    Column("gender", String(255))
)


def start_mappers():
    mapper(model.Employee, employee)
