# both classes are an example of has-a relationship. 
class Other(object):

    def implicit(self):
        print('OTHER implicit()')
    
    def override(self):
        print('OTHER override()')
    
    def altered(self):
        print('OTHER altered()')

class Child(object):

    # this function allows me to take functionality from class Other
    def __init__(self):
        # i'm storing the functions of class Other in self.other
        self.other = Other()

    def implicit(self):
        # this is invoking the functionality of def implicit() in class Other
        self.other.implicit()

    def override(self):
        print('CHILD override()')
    
    def altered(self):
        print('CHILD, BEFORE OTHER altered()')
        # this line allows me to invoke the altered() function in class Other
        self.other.altered()
        print('CHILD, AFTER OTHER altered()')

son = Child()

son.implicit()
son.override()
son.altered()
