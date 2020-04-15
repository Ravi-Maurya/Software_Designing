"""
A client expects to receive family related obj, but don't have to know which family it is until tun time.
It is related to Factory Pattern and concrete product are singletons.
 - Abstract Factory
 - Concrete Factory
 - Abstract Product
 - Concrete Product
 - Client
"""

from abc import ABC, abstractmethod
from typing import Generator


class Pet(ABC):
    """Abstract Interface for pet"""

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def type(self) -> str:
        pass


class Food(ABC):
    """Abstract interface for food"""

    @abstractmethod
    def show(self) -> str:
        pass


class PetFactory(ABC):
    """Abstract interface of pet factory"""

    @abstractmethod
    def pet(self) -> Pet:
        pass

    @abstractmethod
    def food(self) -> Food:
        pass


class PetStore(ABC):
    """Abstract Interface for pet store"""

    @abstractmethod
    def show_pet(self) -> str:
        pass


class Dog(Pet):
    """Dog is Pet"""

    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_

    def speak(self) -> str:
        return f'"{self._name}" says Woof Woof!'

    def type(self) -> str:
        return f"{self._type}"


class DogFood(Food):
    """Dog eats Pedigree"""

    def show(self) -> str:
        return "Pedigree"


class DogFactory(PetFactory):
    """Dog is created"""

    def __init__(self) -> None:
        self._dog: Pet = Dog("Spike", "Bulldog")
        self._food: Food = DogFood()

    def pet(self) -> Pet:
        return self._dog

    def food(self) -> Food:
        return self._food


class Cat(Pet):
    """Cat is Pet"""

    def __init__(self, name: str, type_: str) -> None:
        self._name: str = name
        self._type: str = type_

    def speak(self) -> str:
        return f'"{self._name}" says Meow!'

    def type(self) -> str:
        return f"{self._type}"


class CatFood(Food):
    """Cat eats Milkers"""

    def show(self) -> str:
        return "Milkers"


class CatFactory(PetFactory):
    """Cat is created"""

    def __init__(self) -> None:
        self._cat: Pet = Cat("Cindy", "Persian")
        self._food: Food = CatFood()

    def pet(self) -> Pet:
        return self._cat

    def food(self) -> Food:
        return self._food


class FarmStore(PetStore):
    """Shop is here"""

    def __init__(self, pet_factory: PetFactory) -> None:
        self._pet: Pet = pet_factory.pet()
        self._pet_food: Food = pet_factory.food()

    def show_pet(self) -> Generator[str, None, None]:
        yield f"Our pet is {self._pet.type()}"
        yield f"{self._pet.type()} {self._pet.speak()}"
        yield f"It eats {self._pet_food.show()} food"


if __name__ == '__main__':
    cat_factory: PetFactory = CatFactory()
    store: PetStore = FarmStore(cat_factory)
    print(tuple(store.show_pet()))

    dog_factory: PetFactory = DogFactory()
    store: PetStore = FarmStore(dog_factory)
    print(tuple(store.show_pet()))
