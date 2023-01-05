# this is the module for using arguments
from sys import argv

# i am breaking my argument down into two variables
script, filename = argv

# i have created a file object. this is like creating the machine that will allow me to read the file
txt = open(filename)

# this just prints a message. i am typing sample_text.txt in the terminal to display the argument 'filename'
print(f'Here\'s your file name {filename}:')

# i am printing the variable that stores my filename but without the 'open'
print(txt.read())

# this is printing a message
print('Type the file name again:')

# this is storing an input prompt inside a variable
file_again = input('> ')

# the next two lines are repeating the process
txt_again = open(file_again)

print(txt_again.read())

# this is closing the file
txt_again.close()
