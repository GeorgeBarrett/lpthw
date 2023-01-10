# import argv module
from sys import argv
# import exists. this is a boolean test to see if something exists
from os.path import exists

# argv is broken down into these variables
script, from_file, to_file = argv

# an f string to state the purpose
print(f'Copying from {from_file} to {to_file}')

# turn this into one line
# in_file = open(from_file)
# indata = in_file.read()

indata = open(from_file).read()

# this f string displays the length of file1 in bytes 
print(f'The first file is {len(indata)} bytes long')

# this f string displays if file2 exists and expresses with a boolean value
print(f'Does the ouput file exist? {exists(to_file)}')
print('Ready, hit RETURN to continue or CTRL-C to abort.')
input()

# this varible stores the opening of file2 in write mode
out_file = open(to_file, 'w')
# out_file opens file2 in write mode. write(indata) will write whatever is stored in the variable indata into file2
out_file.write(indata)

print('Alright, all done.')

# always close your files
out_file.close()
