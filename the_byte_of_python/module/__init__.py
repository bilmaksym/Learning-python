# Demo module
def factorial(input):
    '''
    Counts factorial for a given number
    :param input: input variable
    :return: factorial for a given number or None if a number is negative
    '''
    res = 1
    if input < 0:
        return None
    elif input == 0:
        return 1
    else:
        for i in range(1, input + 1):
            res *= i
        return res
    pass


__version__ = '0.1'
