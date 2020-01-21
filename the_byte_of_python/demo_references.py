# Demo program that explains to us how references work
print('Simple Assignment')
shoplist = ['mango', 'apple', 'carrot', 'banana']
mylist = shoplist

# I purchased the first item, so i remove it from the list
del shoplist[0]

print("shoplist is", shoplist)
print('mylist is', mylist)

print('Copy by making a full slice')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

