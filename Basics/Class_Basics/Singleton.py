"""Singleton Pattern says that just"define a class
that has only one instance and provides a global point of access to it". """


class Singleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        """If  instance already exists then don't create it."""
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class A(metaclass=Singleton):
    def __init__(self):
        pass

    def method1(self):
        print("method1")


obj1 = A()
print(obj1)
obj2 = A()
print(obj2)
