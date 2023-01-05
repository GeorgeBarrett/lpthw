types_of_cheese = 1000

# this variable stores another variable in a string
x = f'there are {types_of_cheese} types of cheese'

binary = 'binary'
do_not = 'don\'t'
y = f'there are those who know {binary} and those who {do_not}'

print(f'I say {x}')
print(f'I also say {y}')

hilarious = False

joke_evaluation = 'Is living in a damp overly priced house funny? {}'

# the .format fills in the empty variable slot
print(joke_evaluation.format(hilarious))

print('My favourite climb is {}'.format('Gunshot Wound to the Head'))

print('!' * 100)

# a variable the stores a string of empty objects
formatter = '{} {} {} {}'

# the . format fills in in the empty objects
print(formatter.format(1, 2, 3, 4))

# I have filled in the empty objects with the string of empty objects
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format('lemons', True, 5, 'random'))

# the n means new line and replaces commas, it must also come after a backslash
days = '\nMonday\nTuesday\nWednesday\nMeh'

print(days)

tabbed_in = '\tI\'m tabbed in'
split = 'I\'m split \non a line'
george = 'I\'m \\ George'

chubby_pig = '''
I'll do a list:
\t* I
\t* love
\t* acorns
'''

print(tabbed_in)
print(split)
print(george)
print(chubby_pig)