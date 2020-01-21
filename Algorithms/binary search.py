# Function counts factorial of number
def factorial(input):
    res = 1
    for i in range(1, input+1):
        res *= i
    return res

def binary_search(list, item):

    '''
    Function of binary search finds item of a given list for log2(n) time
    :param list: given list
    :param item: element that we search
    :return: element that we found or None if there is no such element
    '''

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
    return None

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(binary_search(list, 15))
print(factorial(16))