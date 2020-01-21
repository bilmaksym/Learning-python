# Example of __init__ method usage
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Maksym')
p.say_hi()
# The previous 2 lines can be written as Person('Maksym').say_hi()