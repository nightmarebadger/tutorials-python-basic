# -*- coding: utf-8 -*-

"""
    A simple Selection sort implementation:
        http://en.wikipedia.org/wiki/Selection_sort
"""


def selectionSort(li):
    """Find the smallest element and put it in the first position, then find
    the second smallest and put it in the second position and repeat until you
    get to the last position.

    >>> selectionSort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> selectionSort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> selectionSort([3, 2, 6, 1, 4, 2, 3, 1, 1, 5, 6, -2, 2.3])
    [-2, 1, 1, 1, 2, 2, 2.3, 3, 3, 4, 5, 6, 6]
    """

    for i in range(len(li) - 1):
        for j in range(i + 1, len(li)):
            if li[j] < li[i]:
                li[i], li[j] = li[j], li[i]

    return li


if __name__ == "__main__":
    import doctest
    doctest.testmod()
