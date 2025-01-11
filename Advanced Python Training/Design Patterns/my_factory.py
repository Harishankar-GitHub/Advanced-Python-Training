import sys
from abc import ABCMeta, abstractmethod
from venv import create


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def make_noise(self):
        pass

class Dog(Animal):
    def make_noise(self):
        return 'woof'
class Cat(Animal):
    def make_noise(self):
        return 'miaow'
class Lion(Animal):
    def make_noise(self):
        return 'roar'
class Bat(Animal):
    def make_noise(self):
        return '___'

class CreatureFactory():
    def make_sound(self, obj):
        return eval(obj)().make_noise()

if __name__ == '__main__':
    cf = CreatureFactory()
    creature = sys.argv[1]  # here we expect a system argument variable.
    noise = cf.make_sound(creature)
    print(f'The creature {creature} says {noise}')
