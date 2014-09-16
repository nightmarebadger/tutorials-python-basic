# -*- coding: utf-8 -*-

"""
A simple merge sort implementation:
    http://en.wikipedia.org/wiki/Merge_sort
"""


def merge(left, right):
    """Merges ordered lists 'left' and 'right'. It does this by comparing the
    first elements and taking the smaller one and moving on to the next one in
    the list, continuing until it gets to the end of both lists.

    >>> merge([1, 5, 8], [1, 3, 8, 12])
    [1, 1, 3, 5, 8, 8, 12]
    >>> merge([], [1, 2])
    [1, 2]
    >>> merge([1, 2], [])
    [1, 2]
    """

    new = []
    while left and right:
        if left[0] < right[0]:
            new.append(left.pop(0))
        else:
            new.append(right.pop(0))

    new.extend(left)
    new.extend(right)

    return new


def mergeSort(li):
    """Sorts a list by splitting it to smaller and smaller pieces (until they
    only have one or less elements) and then merges it back using the function
    ``merge()``.

    >>> mergeSort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> mergeSort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> mergeSort([3, 2, 6, 1, 4, 2, 3, 1, 1, 5, 6, -2, 2.3])
    [-2, 1, 1, 1, 2, 2, 2.3, 3, 3, 4, 5, 6, 6]
    """

    n = len(li)
    if n < 2:
        return li

    return merge(mergeSort(li[:n//2]), mergeSort(li[n//2:]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
