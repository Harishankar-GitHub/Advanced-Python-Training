from threading import Thread # we can access OS threads via this class
import time
import random

def myFn(n):
    for i in range(0,6):
        print(f'{n} is sleeping')
        time.sleep(random.random()*0.1)

def main():
    # invoke the function on additional threads

    myFn(1) # this is invoked on the main thread
    t1 = Thread(target=myFn, args=(1,), kwargs={}) # to use Threading we target the function
    t2 = Thread(target=myFn, args=(), kwargs={'n' : 2})

    t1.start()
    t2.start()

    print('printing from main thread')

    t1.join()
    t2.join()

    print('printing after t1 and t2 are executed')

if __name__ == '__main__':
    main()
