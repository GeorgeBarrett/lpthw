class Parent(object):
    
    def override(self):
        print('PARENT override()')


class Child(Parent):

    # because I have defined a function within the Child class, the Parent functionality is overwritten
    def override(self):
        print('CHILD override()')

dad = Parent()
son = Child()

dad.override()
son.override()
        