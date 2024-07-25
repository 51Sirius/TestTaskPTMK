from datetime import date

class Employee:
    def __init__(self, first_name: str, last_name: str, midle_name: str, gender: str, birthdate: date):
        self.first_name = first_name
        self.midle_name = midle_name
        self.last_name = last_name
        self.gender = gender
        self.birthdate = birthdate

    def __repr__(self):
        return f"<Employee {self.reference}>"

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    @property
    def full_name(self) -> str:
        return self.last_name + self.first_name  + self.midle_name
