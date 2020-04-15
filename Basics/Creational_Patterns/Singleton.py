"""
Singleton allows only one object to be instantiated from a class template.
Can create a class or can create decorator.
"""

from typing import Dict, Any


class Singleton:
    """Make all instances as the same object."""

    def __new__(cls) -> "Singleton":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance


def singleton(cls: Any) -> Any:
    """A singleton Decorator"""
    instances: Dict[Any, Any] = {}

    def get_instance() -> Any:
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance


@singleton
class Bar:
    """A Class with singleton Decorator"""
    pass


class Borg:
    """Borg class making class attr global.
    Safe the same state of all instances but instances are all Different."""
    _shared_state: Dict[Any, Any] = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared_state


class BorgSingleton(Borg):
    """This class shares all its attr among its instances."""

    def __init__(self, **kwargs: Any) -> None:
        Borg.__init__(self)
        self._shared_state.update(kwargs)

    def __str__(self) -> str:
        return str(self._shared_state)


if __name__ == '__main__':
    obj1: Singleton = Singleton()
    obj2: Singleton = Singleton()
    print(id(obj1))
    print(id(obj2))
    print(obj1 is obj2)

    obj3: Bar = Bar()
    obj4: Bar = Bar()
    print(id(obj3))
    print(id(obj4))
    print(obj3 is obj4)

    x: Borg = BorgSingleton(Obj1=obj1)
    print(x)

    y: Borg = BorgSingleton(Obj2=obj2)
    print(y)
