import the_byte_of_python.module as module
import sys

def total(a, *numbers, **phonebook):
    print("A is", a)

    for i in numbers:
        print('single_item is', i)
    for first_item, second_item in phonebook.items():
        print(first_item, second_item)

#total(10,1,2,3,Ivan=9992515,Natalya=99992551,Lesya='0681629181')


# Example of docstring usage
def find_max():
    ''' This function prints the maximum of two numbers

    @copyright, All rights reserved '''
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))

    print(max(x, y))

#find_max()
#print(find_max.__doc__)

print(module.__version__)
print(module.factorial(10))
print(dir(sys))
