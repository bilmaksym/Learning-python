# This program will be first iteration of class with algoritms


class Algorithms:
    """
    This class has a realization of all algorithms from Bharhava book
    """

    @classmethod
    def factorial_recursion(cls, number):
        """
        This method calc a factorial by a given number
        :param number: input number of factorial
        :return: factorial
        """
        if number == 1:
            return 1
        elif number == 0:
            return 1
        else:
            return cls.factorial_recursion(number - 1)
        pass

    @classmethod
    def selection_sort(cls, array):
        """
        This method shows the work of selection sort algorithm
        """
        new_array = []
        for i in range(len(array)):
            smallest = cls.find_smallest(array)
            new_array.append(array.pop(smallest))
        return new_array
        pass

    @staticmethod
    def find_smallest(array):
        smallest = array[0]
        smallest_index = 0
        for i in range(1, len(array)):
            if array[i] < smallest:
                smallest = array[i]
                smallest_index = i
        return smallest_index
        pass

    @classmethod
    def binary_search(cls, array, item):
        """
        Function of binary search finds item of a given list for log2(n) time
        :param array: given list
        :param item: element that we search
        :return: element that we found or None if there is no such element
        """

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = array[mid]
            if guess == item:
                return mid
            elif guess > item:
                high = mid - 1
            elif guess < item:
                low = mid + 1
        return None
        pass

    @classmethod
    def sum_of_array(cls, array):
        """
        This function calculates sum of array using recursion
        :return: sum of array
        """
        if len(array) == 0:
            return 0
        return array[0] + cls.sum_of_array(array[1:])
        pass

    @classmethod
    def number_of_elements(cls, array):
        """
        This function calculates number of elements in array using recursion
        :param array: A given array
        :return: number of elements in array
        """
        if not array:
            return 0
        return 1 + cls.number_of_elements(array[1:])
        pass

    @classmethod
    def find_max(cls, array):
        if len(array) == 1:
            return array[0]
        elif not array:
            return 0
        temp = cls.find_max(array[1:])
        if array[0] > temp:
            return array[0]
        return temp
        pass

    @classmethod
    def quick_sort(cls, array):
        """
        This function is realisation of quick sort algorithm
        :param array: A given array
        :return: return sorted given array
        """
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot] # a very interesting construction,should learn in future
            greater = [i for i in array[1:] if i > pivot]
        return cls.quick_sort(less) + [pivot] + cls.quick_sort(greater)
        pass


