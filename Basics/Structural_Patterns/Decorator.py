"""
Decorator provides to add the new features to the existing objects, i.e. Dynamic Changes
Can also be implemented in class
"""

from typing import Callable
from functools import wraps


def make_blink(function: Callable[[str], str]) -> Callable[..., str]:
    """Define a Decorator Function"""

    @wraps(function)
    def decorator(*args, **kwargs) -> str:
        result: str = function(*args, **kwargs)
        return f"<blink>{result}</blink>"

    return decorator


@make_blink
def hello(name: str) -> str:
    """Original Function"""
    return f'Hello World says "{name}"!'


if __name__ == '__main__':
    print(hello(name="Ravi"))
    print(hello.__name__)
    print(hello.__doc__)
