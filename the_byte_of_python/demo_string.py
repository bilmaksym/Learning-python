# Demo program that shows me how powerful are python with stings
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
countries = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(countries))

