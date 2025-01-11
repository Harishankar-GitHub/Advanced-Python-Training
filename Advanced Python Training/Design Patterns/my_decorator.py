# There are many decorators built into Python
#@property, @x.setter, @abstractmethod

def showArgs(func): # takes a function as an argument
    '''this function may be used to decorate any other function
        It will reveal all arguments and positional arguments
        Then run the original function'''
    def newFunc(*args, **kwargs):
        '''log the arg/kwarg values'''
        print(f'''Running a function called {func.__name__}
    The positional arguments are {args}
    The keyword arguments are {kwargs}''')
        # remember to call the original function!
        return func(*args, **kwargs)

    return newFunc  # we do not invoke our new function

def notEmpty(func):
    def newFunc(*args, **kwargs):
        '''log the arg/kwarg values'''
        print(f'''Running a function called {func.__name__}
    The positional arguments are {args}
    The keyword arguments are {kwargs}''')
        # remember to call the original function!

        if (len(args) == 0 or len(kwargs) == 0):
            raise TypeError('No arguments provided!')

        for i in args:
            ifEmptyRaiseTypeError(i)
        for i in kwargs:
            ifEmptyRaiseTypeError(i)

        return func(*args, **kwargs)

    def ifEmptyRaiseTypeError(i):
        if i is None or i == "":
            raise TypeError('Argument cannot be empty!')

    return newFunc  # we do no invoke our new function

@notEmpty
# @showArgs # we apply our decorator to this function
def isOdd(n):
    return n%2 != 0

@notEmpty
@showArgs # we apply our decorator to this function
def squares(m,n):
    s = []
    for i in range(m,n):
        s.append(i*i)
    return s

if __name__ == '__main__':
    # print(isOdd(7)) # True
    # print(squares(-2, 3)) # [4,1,0,1,4]
    # print(squares(m=-2, n=3)) # [4,1,0,1,4]

    # print(isOdd())
    print(squares(-2))
