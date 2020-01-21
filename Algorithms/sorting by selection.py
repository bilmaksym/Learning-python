def find_smallest(array):
    '''
    This function finds index of the smallest number in a given array
    :param array: a given array
    :return: index of smallest number
    '''
    smallest = array[0]  # Here we will store smallest number
    smallest_index = 0  # Here we will store index of the smallest item
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    '''
    This function sorts a given array
    :param array: a given array
    :return: sorted array
    '''
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array


array = [5, 3, 6, 2, 10]
print(selection_sort(array))