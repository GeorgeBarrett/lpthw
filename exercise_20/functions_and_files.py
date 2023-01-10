# imports module for arguments
from sys import argv

# the argument is broken down into two variables
script, input_file = argv

# this function has a file passed into its parenthesis
def print_all(f):
    # the function prints the entire file (reads all its bytes)
    print(f.read())

def rewind(f):
    # this inbuilt function will print the file from it's first byte (0)
    f.seek(0)

def print_a_line(line_count, f):
    # f.readline() reads the bytes of the line until there is a new line
    print(line_count, f.readline())

# this stores the opening of the argument (which is test.txt) as a variable
current_file = open(input_file)

print('First, let\'s print the whole file:\n')

# the function is invoked. The variable passed in opens the file. The print_all prints the entire file (f.read())
print_all(current_file)

print('Now, let\'s rewind like a tape.\n')

# the rewind function is invoked which opens the file (every byte) but starts at the first byte (f.seek(0))
rewind(current_file)

print('Let\'s print the three lines again:')

# storing 1 as a variable
current_line = 1

# current_file opens the file. current_line opens the first line. The function print_a_line prints the file but stops at the end of the line
print_a_line(current_line, current_file)

# this redifines the variable so that it is the original variable plus 1 (the plus one moves the ouptut onto the next line of the file)
current_line += 1

print_a_line(current_line, current_file)

# this reads current_line = current_line + 1. shorthand 
current_line += 1

print_a_line(current_line, current_file)

# the print_a_line function is called three times, which tells line_count that there are three lines in the file