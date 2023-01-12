# creating a class
class my_stuff(object):
    
    # a function that prints a message
    def __init__(self):
        self.tangerine = 'And now a thousand years between us.'

    # another function that prints a message
    def apple(self):
        print('I\'m a classy apple.')

# this line instantiates the my_stuff() class into an object
thing = my_stuff()

# now i can call my class 'thing' and fire the apple function 
thing.apple()

# now i can call my class thing and fire the variable that stores a print message
print(thing.tangerine)