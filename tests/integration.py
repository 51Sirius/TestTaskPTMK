import datetime
from sqlalchemy.sql import text
from domain import model
from adapters import repository


def test_repository_can_save_a_employee(session):
    employee = model.Employee("Danil", "Gusev", "Dmitrievich", "Male", "2003.12.23")
    repo = repository.SqlAlchemyRepository(session)
    repo.add(employee)
    session.commit()

    rows = session.execute(
        text('SELECT first_name, last_name, middle_name, gender, birthday  FROM "employee"')
    )
    assert list(rows) == [("Danil", "Gusev", "Dmitrievich", "Male", "2003.12.23"),]
