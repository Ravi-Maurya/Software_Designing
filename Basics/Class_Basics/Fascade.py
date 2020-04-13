"""Facade Design Pattern if class Facade(object)
A Facade Pattern says that just "just provide a unified and
simplified interface to a set of interfaces in a subsystem,
therefore it hides the complexities of the subsystem from
the client".
Facade + Singleton if class Facade(metaclass = Meta) """


class Sensor(object):
    def __init__(self):
        pass

    def sensorOn(self):
        print("Sensor On")

    def sensorOff(self):
        print("Sensor Off")


class Smoke(object):
    def __init__(self):
        pass

    def smokeOn(self):
        print("Smoke On")

    def smokeOff(self):
        print("Smoke Off")


class Lights(object):
    def __init__(self):
        pass

    def lightsOn(self):
        print("Lights On")

    def lightsOff(self):
        print("Lights Off")


class Meta(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(Meta, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class Facade(metaclass=Meta):
    def __init__(self):
        self.__sensor = Sensor()
        self.__smoke = Smoke()
        self.__light = Lights()

    def emergency(self):
        self.__sensor.sensorOn()
        self.__light.lightsOn()
        self.__smoke.smokeOn()

    def noEmergency(self):
        self.__sensor.sensorOff()
        self.__light.lightsOff()
        self.__smoke.smokeOff()


if __name__ == '__main__':
    facade = Facade()
    print(facade)
    facade1 = Facade()
    print(facade1)
    sensor = 22
    if sensor > 25:
        facade.emergency()
    else:
        facade.noEmergency()
