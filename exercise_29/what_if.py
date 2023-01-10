people = 20
mercurians = 30
saturnites = 15

if people < mercurians:
    print('The Mercurians are here in force.')

if people > mercurians:
    print('The Mercurians are a minority.')

if people < saturnites:
    print('The Saturnites are taking over.')

if people > saturnites:
    print('We must welcome the Saturnites.')

# this is redifining the saturnites variable with an extra 5 saturnities
saturnites += 5

if people >= saturnites:
    print('People are greater or equal to Saturnites.')

if people <= saturnites:
    print('People are less than or equal to Saturnites.')

if people == saturnites:
    print('People are Saturnites!')