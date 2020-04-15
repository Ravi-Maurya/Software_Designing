"""
Factory Pattern provides the interface for object Creation.
Defers object instantiation to run time.
 - Product
 - Concrete Product
 - Creator
 - Concrete Creator
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """A shape Interface"""

    @abstractmethod
    def draw(self) -> str:
        pass


class ShapeError(Exception):
    """Error Handler class not related to Factory"""
    pass


class Circle(Shape):
    """Circle is to be drawn"""

    def draw(self) -> str:
        return "Circle.draw"


class Square(Shape):
    """Square is to be drawn"""

    def draw(self) -> str:
        return "Square.draw"


class ShapeFactory:
    """Shape is created"""

    def __init__(self, shape: str) -> None:
        self._shape: str = shape

    def get_shape(self) -> Shape:
        if self._shape == "Circle":
            return Circle()
        if self._shape == "Square":
            return Square()
        raise ShapeError(f'Could not find "{self._shape}" shape!')


if __name__ == '__main__':
    factory: ShapeFactory = ShapeFactory("Circle")
    circle: Shape = factory.get_shape()
    print(circle.__class__.__name__)
    print(circle.draw())

    factory: ShapeFactory = ShapeFactory("Square")
    square: Shape = factory.get_shape()
    print(square.__class__.__name__)
    print(square.draw())