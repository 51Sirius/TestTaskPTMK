from datetime import date
import datetime


class Employee:
    def __init__(self, first_name: str, last_name: str, middle_name: str, gender: str, birthday: date):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday

    def __repr__(self):
        return f"<Employee {self.full_name}>"

    @property
    def full_name(self) -> str:
        return self.last_name + self.first_name + self.middle_name

    @property
    def years(self) -> int:
        now = datetime.datetime.now().date()
        return int((now - self.birthday).days / 365)
