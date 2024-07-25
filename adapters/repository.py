import abc
from domain import model


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, employee: model.Employee ):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Employee :
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, employee):
        self.session.add(employee)

    def get(self, reference):
        return self.session.query(model.Employee).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Employee).all()
