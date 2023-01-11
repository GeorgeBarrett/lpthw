# the initial question
print('''
You enter a room with two doors. \n
Do you go through door #1 or door #2?
''')

# storing a prompt in a variable called door
door = input('> ')

# setting the first condition
if door == '1':
    print('There\'s a giant bear here eating a cheesecake.')
    print('What do you do?')
    print('#1 take the cake.')
    print('#2 scream like a banshee.')

    # storing a prompt in a variable called bear
    bear = input('> ')

    # these react to the inputs of the user. 
    # The else means that any input other than 1 or 2 will have a return value
    if bear == '1':
        print('The bear eats your face off.')
    elif bear == '2':
        print('The bear eats your still pumping heart.')
    else:
        # the {bear} mirrors the user's input
        print(f'Well, doing {bear} is probably better.')
        print('Bear runs away')

elif door == '2':
    print('You stare into the infinte abyss at Cthulhu\'s retina and see.')
    print('1. Blueberries.')
    print('2. Yellow jacket clothespins.')
    print('3. Understanding revolvers yelling melodies.')

    insanity = input('> ')

    # this if and else returns values for the inputs of '1' and '2'
    if insanity == '1' or insanity == '2':
        print('Your body survives powered by a mind of jelly.')
        print('Nice work!')
    else: 
        print('The insanity rots your eyes into a pool of muck.')
        print('Nice work!')

# this final else fires up if the user inputs neither door 1 or door 2
else:
    print('You stumble around and fall on a spoon and die.')