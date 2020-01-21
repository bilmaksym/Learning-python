# Here I will write my first instance of using dictionary

# ab is a short for address book
ab = {
    'Maksym': 'bilmaksym@gmail.com',
    'Natalya': 'ne_bill@gmail.com',
    'Andrey': 'bil1977@gmail.com',
    'Swaroop': 'swaroop@swaroopch.org'
}
print('Maksym\'s address is ', ab['Maksym'])

# deleting a pair
del ab['Andrey']
print('\nThere are {} contacts in address book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
