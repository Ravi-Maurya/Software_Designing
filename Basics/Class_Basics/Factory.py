"""Factory Design Pattern
Factory Method Pattern says that just define an interface or abstract class for creating an
object but let the subclasses decide which class to instantiate. In other words, subclasses are responsible to create
the instance of the class. """


class A(object):
    def __init__(self):
        pass

    def print(self):
        print("Method A")


class B(object):
    def __init__(self):
        pass

    def print(self):
        print("Method B")


class Factory(object):
    def __init__(self):
        pass
    @staticmethod
    def get(obj=''):
        objs = dict(a=A(), b=B())
        return objs[obj]


a = Factory().get('a')
a.print()
b = Factory().get('b')
b.print()
