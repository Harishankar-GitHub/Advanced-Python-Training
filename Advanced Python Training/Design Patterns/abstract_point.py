import abc

# we can declare an abstract class to enforce rules on our concrete classes
class Planar(metaclass=abc.ABCMeta):
    # Abstraction for a planar point x and y
    def __init__(self):
        pass

    @abc.abstractmethod
    def hypotenuse(self):
        pass

# we implement no actual functionality

class InsistStr(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass
