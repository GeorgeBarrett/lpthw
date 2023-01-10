# defining a function that has two arguments.
def add(a, b):
    print(f'adding {a} + {b}')
    # this return statement means I can store the function and its arguments in a variable
    return a + b

def subtract(a, b):
    print(f'subtracting {a} - {b}')
    return a - b

def multiply(a, b):
    print(f'multiplying {a} * {b}')
    return a * b

def divide(a, b):
    print(f'dividing {a} / {b}')
    return a / b

print('Let\'s do some math with just functions!')

# these are the functions and their arguments being stored as variables
age = add(30, 5)
height = subtract(7, 0.7)
weight = multiply(6, 2)
iq = divide(100, 2)

print(f'Age: {age}, Height: {height}, Weight: {weight}, Iq: {iq}')

print('Here is a puzzle.')

# this is a variable that stores the math results of multiple functions and their arguments
# notice how the formula works inside out, starting with 'iq', which = 50 being divided by 2.
# a variable and math '2' are being used as the arguments for the divide function  
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print('That becomes', what, 'Can you do it by hand?')