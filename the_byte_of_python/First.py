age = 19

name = 'Maksym'

# Usage of format method
print("{name} was {age} years old when he started studying python".format(name=name, age=age))
print("Why is {name} playing with that python?".format(name=name))

# Usage of f in version that after python 3.6
print(f"{name} was {age} years old when he started studying python")
print(f"Why is {name} playing with that python?")

# Declaring first function
def while_loop():
    # Another interesting example
    while True:
        x = input("Enter some phrase:")
        if x == "quit":
            break
        elif len(x) < 3:
            print("Too short!")
            continue
        print('Phrase is of sufficient length')

# Example with declaring global variable within the function
x = 50
def do_something():
    global x
    print('X is', x)
    x = 2
    print('Global changed, now =', x)
do_something()
print('X now is', x)

# Example of function with default arguments
def say(message, times=2):
    print(message * times)

msg = "Kalyan petuh \n"
say(msg)
say(msg, 10)
