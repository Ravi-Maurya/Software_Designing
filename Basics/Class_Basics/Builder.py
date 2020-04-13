"""Builder Pattern says that "construct a complex object from simple objects using step-by-step approach" ."""


class A(object):
    def __init__(self, obj):
        self.variable = obj.variable

    def print(self):
        print(self.variable)

    class Builder:
        def __init__(self):
            self.variable = None

        def set_var(self, variable):
            self.variable = variable
            return self

        def build(self):
            a = A(self)
            return a


obj1 = A.Builder().set_var("Builder is Created and Executed").build()
obj1.print()