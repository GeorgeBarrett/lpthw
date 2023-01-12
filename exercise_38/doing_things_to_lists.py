# a variable containing a single string of 6 things
ten_things = 'Apples Oranges Crows Telephone Light Sugar'

# I want 10 things in the list
print('Hold on! There aren\'t ten things in that list')

# this variable stores ten_things. the .split() converts the string into a list
stuff = ten_things.split(' ')

# this is a variable that stores a list of strings. each one being a word
more_stuff = ['Day', 'Night', 'song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# this loops through the stuff list until 10 items are included. 11 would return false
while len(stuff) != 10:
    # this variable removes last words from more_stuff until stuff has ten words
    next_one = more_stuff.pop()
    
    # the while loop prints the popped words incrementally
    print('Adding: ', next_one)
    
    # once the while loop has returned false, the new words (which make up ten) will be added to stuff
    stuff.append(next_one)
    
    # this uses an f string to print how many items there are now in stuff
    print(f'There are {len(stuff)} items now.')

# we know have a list with ten things!
print('There we go: ', stuff)

print('Let\'s do some things with stuff.')

# this will print the second item in the list 
print(stuff[1])

# this will print the last item in the list
print(stuff[-1])

# this will remove the last word in the list
print(stuff.pop())

# this will turn stuff from a list into a single string
print(' '.join(stuff))

# this will print the 3rd and 4th items in the string
print(' '.join(stuff[3:5]))
