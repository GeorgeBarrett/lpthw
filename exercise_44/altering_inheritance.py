# creating a class which is a container for functions etc
class Parent(object):

    # this function prints a statement
    def altered(self):
        print('PARENT altered()')

# class Child inherits the functionality of class Parent
# i can type 'pass' within this class and the functionality will remain the same
# this is good for repetitive code but bad for storing classes within variables
class Child(Parent):

    # because I have not typed 'pass' and instead defined a function the inheritance will be overridden
    def altered(self):
        
        # without the super function then PARENT altered() would be printed
        print('CHILD, BEFORE PARENT altered()')
        
        # python's super function can overide instances
        # the .altered() overrides the newly defined functionality of the class Child thus reverting back to the class Parent functionality
        super(Child, self).altered()
        print('CHILD, AFTER PARENT altered()')

# instantiating the classes into objects
dad = Parent()
son = Child()

# calling the objects and firing their functions
dad.altered()
son.altered()