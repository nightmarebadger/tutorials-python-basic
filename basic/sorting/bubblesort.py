# -*- coding: utf-8 -*-

"""
A simple Bubble sort implementation:
    http://en.wikipedia.org/wiki/Bubble_sort
"""


def bubbleSort(li):
    """Compare adjecent pairs and turn them around if they're not sorted
    properly, therefore "bubbling" higher elements to the end and lower
    elements to the beginning. We need to do it a maximum of len(li) times.

    >>> bubbleSort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> bubbleSort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bubbleSort([3, 2, 6, 1, 4, 2, 3, 1, 1, 5, 6, -2, 2.3])
    [-2, 1, 1, 1, 2, 2, 2.3, 3, 3, 4, 5, 6, 6]
    """

    n = len(li)
    for i in range(n):
        for j in range(1, n):
            if li[j-1] > li[j]:
                li[j-1], li[j] = li[j], li[j-1]

    return li


def bubbleSort_smarter(li):
    """Same as above, but we stop as soon as no changes are made (which means
    the list is sorted). We also don't need to go through the whole list on
    each iteration, as each iteration will push the highest element to the end,
    meaning we can ignore it in the next iteration.

    >>> bubbleSort_smarter([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> bubbleSort_smarter([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bubbleSort_smarter([3, 2, 6, 1, 4, 2, 3, 1, 1, 5, 6, -2, 2.3])
    [-2, 1, 1, 1, 2, 2, 2.3, 3, 3, 4, 5, 6, 6]
    """

    n = len(li)
    step = 0
    changed = True
    while changed:
        changed = False
        for i in range(1, n-step):
            if li[i-1] > li[i]:
                li[i-1], li[i] = li[i], li[i-1]
                changed = True

    return li


if __name__ == "__main__":
    import doctest
    doctest.testmod()
