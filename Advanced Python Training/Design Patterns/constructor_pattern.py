from abstract_point import Planar

class Point(Planar): # class Point: also works.
    __slots__ = ('__x', '__y') # constrain this class to allow only these properties

    def __init__(self, x, y): # constructor
        self.x = x # here we call the SETTER Method
        self.y = y # here we call the SETTER Method
        # self.x calls x() method and passes x (which is on the right) as the arguments.

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) in (int,float):
            self.__x = new_x
        else:
            raise TypeError('X must be numeric')

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) in (int,float):
            self.__y = new_y
        else:
            raise TypeError('Y must be numeric')

    def __str__(self):
        # This is similar to toString() method in Java.
        # This method overrides the built-in __str__ and is used by 'print()'
        return f'This point is at ({self.x},{self.y}), hypotenuse {self.hypotenuse()}'

    def __repr__(self):
        # This overrides the built-in __repr__ used in immediate Python
        # For example, x is an object.
        # In terminal, if we type x and enter, it prints the object using __repr__.
        # If we print(x), it prints using __str__.
        return f'Point at {self.x},{self.y}'

    def hypotenuse(self):
        h = (self.x**2 + self.y**2) **0.5
        return h


if __name__ == '__main__':
    p1 = Point(4,3) # this will call the property setter for x and y, thereby validating x and y.
    # p2 = Point(4, '3')  # this will call the property setter for x and y, thereby validating x and y.
    p1.x = 5
    print(p1.x, p1.y)
    # p1.y = [] # this raises type error.

    print(p1)

    print("Hypotenuse")
    print(p1.hypotenuse())
