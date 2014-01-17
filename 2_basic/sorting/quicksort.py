# -*- coding: utf-8 -*-

"""
    A simple quick sort implementation:
        http://en.wikipedia.org/wiki/Quicksort
"""


def quickSort(li):
    """Sort a list by choosing a pivot and putting all lesser elements to one
    side and all greater elements to the other side. Repeat on each side and
    add them back together.

    >>> quickSort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> quickSort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> quickSort([3, 2, 6, 1, 4, 2, 3, 1, 1, 5, 6, -2, 2.3])
    [-2, 1, 1, 1, 2, 2, 2.3, 3, 3, 4, 5, 6, 6]
    """

    if len(li) < 2:
        return li

    pivot = li[0]
    lesser = []
    greater = []

    for el in li[1:]:
        if el <= pivot:
            lesser.append(el)
        else:
            greater.append(el)

    return quickSort(lesser) + [pivot] + quickSort(greater)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
