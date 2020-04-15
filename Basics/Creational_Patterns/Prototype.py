"""
Prototype related to abstract factory patterns
It make copies of the object.
 - Prototype
 - Concrete Prototype
 - Client
"""

import copy
from abc import ABC, abstractmethod
from typing import Dict, Any


class Machine(ABC):
    """Abstract Machine Interface"""

    @abstractmethod
    def info(self) -> str:
        pass


class Car(Machine):
    """A car object"""

    def __init__(self) -> None:
        self._name: str = "Bentley"
        self._color: str = "Royal Blue"
        self._options: str = "Ex"

    def info(self) -> str:
        return "Car details: {} | {} | {}".format(self._name, self._color, self._options)


class Prototype:
    """A Prototype object"""

    def __init__(self) -> None:
        self._elements: Dict[Any, Any] = {}

    def register(self, name: str, machine: Machine) -> None:
        self._elements[name] = machine

    def unregister(self, name: str) -> None:
        del self._elements[name]

    def clone(self, name: str, **kwargs: Any) -> Car:
        obj: Any = copy.deepcopy(self._elements[name])
        obj.__dict__.update(kwargs)
        return obj


if __name__ == '__main__':
    primary_car: Machine = Car()
    print(primary_car.info())

    prototype: Prototype = Prototype()
    prototype.register("Bentley2", primary_car)
    cloned_car: Machine = prototype.clone("Bentley2")
    print(cloned_car.info())
