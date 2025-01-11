from _on import On
from _off import Off
from _sleep import Sleep
from _hibernate import Hibernate
from _laptop import Laptop

def main():
    c = Laptop() # initially laptop is off
    c.change(On)
    c.change(Off)
    c.change(On)
    c.change(Sleep)
    c.change(On)
    c.change(Sleep)
    c.change(Hibernate)
    c.change(On)
    c.change(Hibernate)
    c.change(Off)

if __name__ == '__main__':
    main()
