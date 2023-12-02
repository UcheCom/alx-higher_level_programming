#!/usr/bin/python3
"""This finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function finds a peak in a list
    Args:
        list_of_integers: List of unsorted integers
    Return:
        a peak or None
    """
    if(list_of_integers) == []:
        return None
    size = list_of_integers[:]
    size_t = len(size)
    mid = (size_t) // 2

    if (mid - 1) == -1 and (mid + 1) == size_t:
        return size[mid]

    if (mid - 1) == -1:
        return size[mid] if size[mid] > size[mid + 1] else size[mid + 1]

    if (mid + 1) == size_t:
        return size[mid] if size[mid] > size[mid - 1] else size[mid - 1]

    if size[mid - 1] < size[mid] > size[mid + 1]:
        return size[mid]

    if size[mid + 1] > size[mid - 1]:
        return find_peak(size[mid:])
    return find_peak(size[:mid])
