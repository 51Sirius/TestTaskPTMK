import datetime
from sqlalchemy.sql import text
from domain import model
from adapters import repository


def test_repository_can_save_a_employee(session):
    time = datetime.datetime.now() - datetime.timedelta(days=3*365)
    employee = model.Employee("Danil", "Gusev", "Dmitrievich", "Male", time)
    repo = repository.SqlAlchemyRepository(session)
    repo.add(employee)
    session.commit()

    rows = session.execute(
        text('SELECT first_name, last_name, middle_name, gender, birthday  FROM "employee"')
    )
    assert list(rows) == [("Danil", "Gusev", "Dmitrievich", "Male", time.strftime("%Y-%m-%d")),]
