"""
Participants-
 - Director
 - Abstract Builder: Interface
 - Concrete Builder: Implements the interface
 - Product: Object Being Built
"""
from abc import ABC, abstractmethod


class Machine(ABC):
    """Abstract Machine Interface"""

    @abstractmethod
    def info(self) -> str:
        pass


class Builder(ABC):
    """Abstract Builder Interface"""

    @abstractmethod
    def add_model(self) -> None:
        pass

    @abstractmethod
    def add_tires(self) -> None:
        pass

    @abstractmethod
    def add_engine(self) -> None:
        pass

    @abstractmethod
    def machine(self) -> Machine:
        pass


class Car(Machine):
    """A Car from Machine"""

    def __init__(self) -> None:
        self.model: str = ''
        self.tires: str = ''
        self.engine: str = ''

    def info(self) -> str:
        return "Car Detais: {} | {} | {}".format(self.model, self.tires, self.engine)


class BentleyBuilder(Builder):
    """Provides parts and tools to work on car parts"""

    def __init__(self) -> None:
        self.__car: Machine = Car()

    def add_model(self) -> None:
        self.__car.model = "Bentley"

    def add_engine(self) -> None:
        self.__car.engine = "V8  Engine"

    def add_tires(self) -> None:
        self.__car.tires = "Turbo MRF"

    def machine(self) -> Machine:
        return self.__car


class Director:
    """A director is responsible for car Assembling"""

    def __init__(self, builder__: Builder) -> None:
        self.__builder: Builder = builder__

    def construct_machine(self) -> None:
        self.__builder.add_model()
        self.__builder.add_tires()
        self.__builder.add_engine()

    def release_machine(self) -> Machine:
        return self.__builder.machine()


if __name__ == '__main__':
    builder: Builder = BentleyBuilder()
    director: Director = Director(builder)
    director.construct_machine()
    car: Machine = director.release_machine()
    print(car.info())
