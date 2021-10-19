"""Binary search function"""


def binary(array, key):
    """
    This function realise binary search
    :param key: element for searching
    :type key: int or double
    :param array: array for searching
    :type array: my_array.array
    :return right_side: result
    :rtype: int
    """
    if not array:
        return None
    left_side = -1
    right_side = len(array)
    while right_side > left_side + 1:
        middle = (left_side + right_side) // 2
        if array[middle] >= key:
            right_side = middle
        else:
            left_side = middle
    if key > array[array.length - 1] or key < array[0]:
        return None
    return right_side
