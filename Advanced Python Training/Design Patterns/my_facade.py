# we need to bring together different
from DesignPatterns.abstract_point import InsistStr


class Coder(InsistStr):
    def __init__(self):
        print('Write some code')
    def __is_available(self):
        print('Coding skills are available')
        return True
    def book_time(self):
        if self.__is_available():
            print('Coder has been booked')
    def __str__(self):
        pass

class Tester(InsistStr):
    def __init__(self):
        print('preparing some tests')
    def testing(self):
        print('tests are in place')
    def __str__(self):
        pass

class Technician(InsistStr):
    def __init__(self):
        print('preparing equipment for the team')
    def doStuff(self):
        print('network, machines, cloud all in place')
    def __str__(self):
        pass

class Artisan(InsistStr):
    def __init__(self):
        print('designing things')
    def make_prototype(self):
        print('wireframes are ready')
    def __str__(self):
        pass

class Manager(InsistStr):
    # The manager is the facade to the team members.
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        # the facade provides instances of all other subsystems/microservices
        self.coder = Coder()
        self.tester = Tester()
        self.technician = Technician()
        self.artisan = Artisan()

        self.coder.book_time()
        self.tester.testing()
        self.technician.doStuff()
        self.artisan.make_prototype()
    def __str__(self):
        pass

class Client():
    def __init__(self):
        print('We need a team for our project')
    def askManager(self):
        print('Lets talk to the manager')
        self.manager = Manager()        # here we access the facade
        self.manager.arrange()            # ask the facade to sort things out for us
    def __del__(self):
        # This is destructor method.
        print('all done')

if __name__ == '__main__':
    cust = Client()
    cust.askManager()

    coder = Coder()
