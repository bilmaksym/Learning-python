# This module demonstrates how to work with lists
shoplist = ['FarCry5', 'The Witcher 3', 'Assasin\'s Creed Origins', 'Dishonored 2']

print('I have', len(shoplist), 'games to purchase')

print("These games are", end=' ')
for game in shoplist:
    print(game, end=' ')

print('\nAlso I have to buy Wolfenstein The New Order')
shoplist.append('Wolfenstein The New Order')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I would buy is' \
      , shoplist[0])
old_item = shoplist[0]
del shoplist[0]
print('I\'ve already bought', old_item)
print('My shopping list is now', shoplist)
print()
print(shoplist.index('FarCry5'))