#!python


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_recursive(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index    # Item found
    return None             # Item not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index < len(array):
        if item == array[index]:
            return index        # Item found
        else:
                                # Recursive call
            return linear_search_recursive(array, item, index + 1)
    return None                 # Item not found


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    start_index = 0
    end_index = len(array) - 1

    while end_index >= start_index:
        middle_index = int((start_index + end_index) / 2)
        value = array[middle_index]
        if item == value:
            return middle_index         # Item found
        else:
            if item > value:        # Item in end part of array
                start_index = middle_index + 1
            else:                   # Item in start part of array
                end_index = middle_index - 1

    return None                         # Item not found


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    # Setting up variables if this is the first call
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    else:
        if left > right:
            return None                         # Item not found

    middle_index = int((left + right) / 2)
    value = array[middle_index]
    if item == value:
        return middle_index                     # Item found
    else:
        if item > value:            # Item in end part of array
            return binary_search_recursive(array, item, middle_index + 1, right)
        else:                       # Item in start part of array
            return binary_search_recursive(array, item, left, middle_index - 1)
