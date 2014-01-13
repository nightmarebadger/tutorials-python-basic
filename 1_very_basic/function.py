"""
    A function creation and call example.
"""


def add(x, y):
    """A function that adds x and y together.

    >>> add(1, 5)
    6
    >>> add(-8, 2.7)
    -5.3
    """

    return x + y

if __name__ == "__main__":
    import doctest
    doctest.testmod()
