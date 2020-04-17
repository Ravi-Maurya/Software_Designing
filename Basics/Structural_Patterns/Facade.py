"""
Simpler unified interface to more complex system.
Provides an easier way to access functions of underlying system by providing single entry point.
"""

from abc import ABC, abstractmethod
import time
from typing import List, Tuple, Iterator, Type

_sleep: float = 0.2


class TestCase(ABC):
    """Abstract test case interface"""

    @abstractmethod
    def run(self) -> None:
        pass


class TestCaseOne(TestCase):
    """Concrete class"""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("setting up test case 1")
        time.sleep(_sleep)
        print("Running")
        time.sleep(_sleep)
        print("Tearing")
        time.sleep(_sleep)
        print("Finished 1\n")


class TestCaseTwo(TestCase):
    """Concrete class"""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("setting up test case 2")
        time.sleep(_sleep)
        print("Running")
        time.sleep(_sleep)
        print("Tearing")
        time.sleep(_sleep)
        print("Finished 2\n")


class TestCaseThree(TestCase):
    """Concrete class"""

    def __init__(self, name: str) -> None:
        self._name: str = name

    def run(self) -> None:
        print("{:#^20}".format(self._name))
        time.sleep(_sleep)
        print("setting up test case 3")
        time.sleep(_sleep)
        print("Running")
        time.sleep(_sleep)
        print("Tearing")
        time.sleep(_sleep)
        print("Finished 3\n")


class TestSuite:
    """Represent Simpler unified interface to run all tests
    Facde Class. """

    def __init__(self, testcases: List[TestCase]) -> None:
        self._testcase = testcases

    def run(self) -> None:
        for testcase in self._testcase:  # type: TestCase
            testcase.run()


test_cases: List[TestCase] = [TestCaseOne("TC1"), TestCaseTwo("TC2"), TestCaseThree("TC3")]
test_suite = TestSuite(test_cases)
test_suite.run()


class Interface(ABC):
    """Abstract interface."""

    @abstractmethod
    def run(self) -> str:
        pass


class A(Interface):
    """Implement interface."""

    def run(self) -> str:
        return "A.run()"


class B(Interface):
    """Implement interface."""

    def run(self) -> str:
        return "B.run()"


class C(Interface):
    """Implement interface."""

    def run(self) -> str:
        return "C.run()"


class Facade(Interface):
    """Facade object."""

    def __init__(self):
        self._all: Tuple[Type[Interface], ...] = (A, B, C)

    def run(self) -> Iterator[Interface]:
        for obj in self._all:  # type: Type[Interface]
            yield obj


if __name__ == "__main__":
    print(*(cls().run() for cls in Facade().run()))
