# creating a class. these are like containers for functions and data
class song(object):
    
    # the self is creating an instance which reduces ambiguity
    # this function constructs the object
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # this function controls the actions
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# these two variables instantiate the song class into an objects that contains lyrics
push_it = song (['I saw the gap again today',
                 'While you were begging me to stay',
                 'Take care not to make me enter',
                 'If I do, we both may disappear'])

schism = song (['The poetry that comes from',
                'The squaring off between',
                'And the circling is worth it',
                'Finding beauty in the dissonance'])

# this calls the variable push_it, which stores the functionality and lyrics
# and then invokes the function 
push_it.sing_me_a_song()

schism.sing_me_a_song()
