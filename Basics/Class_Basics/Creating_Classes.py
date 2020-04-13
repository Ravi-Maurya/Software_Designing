class A(object):
    def __init__(self):
        print("Memory is allocated in heap  and then instance is created of Class A")


class B(object):
    def __call__(cls, *args, **kwargs):
        print("Memory is allocated in heap  and then instance is created of Class B")
        return super(B, cls).__call__(*args, **kwargs)

    def __init__(self):
        super(B, self).__init__()


class C(object):
    def __new__(cls, *args, **kwargs):
        print("Memory is allocated in heap of Class C")
        return super(C, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print("Created Instance of Class C")


class F(type):
    def __call__(cls, *args, **kwargs):
        return super(F, cls).__call__(*args, **kwargs)

    def __init__(cls, *args, **kwargs):
        super(F, cls).__init__(*args, **kwargs)


class D(metaclass=F):
    pass


a = A()
print(a)
b = B()
print(b)
c = C()
print(c)
d = D()
print(d)
