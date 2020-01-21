# Always use parentheses
# to indicate start and end of a tuple
# Explicit is better than implicit
zoo = ('monkey', 'elephant', 'penguin')
print('Number of animals in the zoo', len(zoo))

# Here parentheses is not required but it's better to use them
new_zoo = 'python', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo is', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal from old zoo is', new_zoo[2][2])
print('Number of animals in new zoo is', len(new_zoo)-1+len(new_zoo[2]))
