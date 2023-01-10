# importing argv module
from sys import argv

# breaking argv down into modules 
script, filename = argv

# prompts for the user. the f string alllows the filename to be displayed
print(f'We are going to erase {filename}.')
print('If you don\'t want that then hit CTRL-C.')
print('If you do want that then hit RETURN')

# prompts a user input
input('?')

print('Opening the file...')
# stores the opening of the file in write mode as a variable named target
target = open(filename, 'w')

print('Truncating the file. Goodbye!')
# target stores the opened file. .truncate() deletes the file IN WRITE MODE, not the file itself
target.truncate()

print('Now I am going to ask you for three lines.')
# these variables store the user inputs. the inputs include prompts
line1 = input('Line 1: ')
line2 = input('Line 2: ')
line3 = input('Line 3: ')

print('I\'m going to write these to the file.')

# target opens the file. write initiates write mode lol. the variable or string is then added to the text file
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And lastly, close it.')
# target opens the text file in write mode. .close() closes the file
target.close()