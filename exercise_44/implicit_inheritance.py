# creating a class
class Parent(object):

    # function that prints a statement
    def implicit(self):
        print('PARENT implicit()')

# creating a second class that inherits the functionality from the class above
class Child(Parent):
    pass

# instatiating two classes into objects
dad = Parent()
son = Child()

# invoking both objects with their functionality
dad.implicit()
son.implicit()  

# both outcomes are the same. because the Child class has no functionality, it inherits everything from its parent.
