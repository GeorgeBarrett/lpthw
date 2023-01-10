# variables storing numbers
people = 30
cars = 40
trucks = 15

if cars > people:
    print('We better take the cars.') # because there are more cars

elif cars < people:
    print('Cars aren\'t going to cut it.') # because there are too many people

else:
    print('We can\'t decide.') # the final return

if trucks > cars:
    print('TOO MANY TRUCKS.')

elif trucks < cars:
    print('We could use the trucks.')

else:
    print('We still can\'t decide.')

if people > trucks:
    print('It\'s truck time.') # you can get loads of people in trucks

else:
    print('Let\'s just stay in.') # the final return


# if - is the original condition
# elif - fires if the original if returns false
# else - will fire when the if and elif return false
# python will run the first condition that returns true!