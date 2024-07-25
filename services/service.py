from __future__ import annotations
from datetime import date

from domain import model
from adapters.repository import AbstractRepository


def add_employee(first_name: str, last_name: str, middle_name: str, gender: str, birthdate: str,
                 repo: AbstractRepository, session) -> None:
    repo.add(model.Employee(first_name, last_name, middle_name, gender, birthdate))
    session.commit()
