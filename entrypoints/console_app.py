import time
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from mimesis import Person
from mimesis.enums import Gender
from adapters.orm import metadata, start_mappers
import config
import datetime
from domain import model
from adapters import repository
from domain.model import Employee
import time


def start_app(param_to_start: int = 1, args: list = None):
    engine = create_engine("sqlite:///test.sqlite")
    metadata.create_all(engine)
    start_mappers()
    session = scoped_session(sessionmaker(bind=engine))
    if param_to_start == 1:
        print("Tables was created")
    elif param_to_start == 2:
        first_name, last_name, middle_name = args[0].split()
        birthdate = datetime.datetime.strptime(args[1], '%Y-%m-%d')
        gender = args[2]
        employee = Employee(first_name, last_name, middle_name, gender, birthdate)
        repo = repository.SqlAlchemyRepository(session)
        repo.add(employee)
        session.commit()
        print(f"User - {employee.first_name} {employee.last_name} was added to database")
    elif param_to_start == 3:
        employees = session.query(Employee).order_by(Employee.first_name.desc(), Employee.middle_name.desc(),
                                                     Employee.last_name.desc(), Employee.birthday.desc()).distinct(
            Employee.first_name.desc(), Employee.middle_name.desc(),
            Employee.last_name.desc(), Employee.birthday.desc()).all()
        for employee in employees:
            print(employee.full_name, employee.birthday, employee.years)

    elif param_to_start == 4:
        person = Person('en')
        employees = []
        for _ in range(0, 500000):
            employees.append(
                Employee(person.first_name(gender=Gender.MALE), person.last_name(gender=Gender.MALE),
                         person.last_name(gender=Gender.MALE), "Male", person.birthdate()))
        for _ in range(0, 500000):
            employees.append(
                Employee(person.first_name(gender=Gender.FEMALE), person.last_name(gender=Gender.FEMALE),
                         person.last_name(gender=Gender.FEMALE), "Female", person.birthdate()))
        for _ in range(0, 100):
            employees.append(
                Employee(person.first_name(gender=Gender.MALE), "F" + person.last_name(gender=Gender.MALE),
                         person.last_name(gender=Gender.MALE), "Male", person.birthdate()))
        session.bulk_save_objects(employees)
        session.commit()
    elif param_to_start == 5:
        start_time = time.time()
        employees = session.query(Employee).filter(Employee.gender == "Male", Employee.last_name.startswith('F')).all()
        end_time = time.time()
        elapsed_time = end_time - start_time
        for employee in employees:
            print(employee.full_name, employee.birthday, employee.years)
        print('Elapsed time: ', elapsed_time)
    elif param_to_start == 6:
        start_time = time.time()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Elapsed time: ', elapsed_time)
