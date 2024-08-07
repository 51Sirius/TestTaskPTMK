from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship, registry

from domain import model


metadata = MetaData()
mapper_registry = registry(metadata=metadata)

employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(255)),
    Column("last_name", String(255), index=True),
    Column("middle_name", String(255)),
    Column("birthday", Date),
    Column("gender", String(10), index=True)
)


def start_mappers():
    mapper_registry.map_imperatively(model.Employee, employee)
