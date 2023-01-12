# is-a
class Animal(object):
    pass

# has-a
class Dog(Animal):

    def __init__(self, name):
        self.name = name

# has-a
class Cat(Animal):

    def __init__(self, name):
        self.name = name


# is-a
class Person(object):

    def __init__(self, name):
        self.name = name


# has-a
class Employee(Person):
    
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


# is-a
class Fish(object):
    pass


# has-a
class Cod(Fish):
    pass


# has-a
class Tuna(Fish):
    pass


# is-a
rover = Dog('Rover')

# is-a
satan = Cat('Satan')

# is-a
george = Person('George')

# has-a
george.pet = satan

# is-a
roly = Employee('Roly', 1000000)

# has-a
roly.pet = rover

# has-a
flipper = Fish()

# is-a
aphra = Cod()

# is-a
tev = Tuna()

