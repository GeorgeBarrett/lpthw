formatter = '{} {} {} {}'

print(formatter.format(1, 2, 3, 4))
print(formatter.format(True, False, True, False))
print(formatter.format('1', '2', '3', '4'))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    'I love my standing desk',
    'It keeps me straight and tall',
    'If I was to lose it',
    'I would have to... buy another one'
))