# this is defining a function with two variables
def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f'You have {cheese_count} cheeses!')
    print(f'You have {box_of_crackers} boxes of crackers!')
    print('That\'s not enough')
    print('Better get some more.\n')

print('We can just give the function numbers directly:')
# this is invoking the function and assigning numbers to the variables inside the function 
cheese_and_crackers(20, 30)

print('OR, we can use variables from our script:')
# this is storing numbers as variables
amount_of_cheese = 50
amount_of_crackers = 30

# this is invoking the function and then passing the variables which store numbers into it
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print('We can even do math inside too:')
# this is invoking the function but doing math rather than passing numbers directly
cheese_and_crackers(10 + 20, 15 + 15)

print('And we can combine the two, variables with math:')
# this is invoking the function and passing the variables (which store numbers) along with math into it 
cheese_and_crackers(amount_of_cheese * 100, amount_of_crackers + 500)