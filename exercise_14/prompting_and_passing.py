from sys import argv

script, user_first_name, user_last_name  = argv
prompt = '> '

print(f'Hi {user_first_name} {user_last_name}, I\'m the {script} script')
print('I\'d like to ask a few questions')

print(f'Do you like me {user_first_name} {user_last_name}?')

# the prompt is just a prompt to type
likes = input(prompt)

print(f'Where do you live {user_first_name} {user_last_name}')
lives = input(prompt)

print(f'What is your favourite film {user_first_name} {user_last_name}')
favourite_film = input(prompt)

print(f'''
Alright, so you said {likes} about liking me. You live in {lives},
and your favourite film is {favourite_film}.
 ''')

# using arguments is handy as only a small amount of code needs to be changed.
# change the arguments and the rest of the script changes with it

# the last print just outputs the prompts
# the arguments are given in the terminal in sequential order