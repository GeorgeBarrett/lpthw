# escapes
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes \\ with that do:')
print('\n new lines and \t tabs')

# poem using escapes stored within a self titled variable
poem = '''
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanantion
\n\t\twhere there is none.
'''

# printing the poem with some string decoration
print('----------')
print(poem)
print('----------')

# storing math within a variable and printing it using an f string
five = 10 - 2 + 3 - 6
print(f'This should be five: {five}')

# function that has a variable
# the started variable is needed to ignite the math sequence 
def secret_formula(started):
    # this is accumulative math stored in variables. reading it backwards makes more sense
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    
    # this return statement means the variables can be called upon later
    return jelly_beans, jars, crates

# this is a new variable that stores the number 10000
start_point = 10000

# these three variables store the secret_formula function with start_point (10000) passed in
# I can redifine jelly_beans as beans because the variable is being passed through within the function secret_formula
beans, jars, crates = secret_formula(start_point)

# this prints out 10000 inside the braces but using .format(variable) rather than an f string
print('With a starting point of: {}'.format(start_point))

# this uses an f string to display the variables that hold the math in secret_formula
print(f'We\'d have {beans} beans, {jars} jars and {crates} crates')

# this is redifining the start_point variable with more math
# why am I dividing this by ten?
start_point = start_point / 10

print('We can also do that this way:')

# this variable stores all of the math from secret_formula with the redefined start_point variable passed in 
formula = secret_formula(start_point)

# the *formula fills the empty curly braces with all the elements of formula in numerical order
print('We\'d have {} beans, {} jars and {} crates'.format(*formula))