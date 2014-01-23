# -*- coding: utf-8 -*-

"""
    Remember that the variables passed to a function are local, even if they
    are named the same as one of the "outside" variables.
"""


def add_one_and_print(x):
    """Add one to the number and print it, showcasing local variables.

    Let's create a variable named x and set it to a number

    >>> x = 5

    Let's call the function

    >>> add_one_and_print(x)
    6

    Obviously the 'x' inside the function changed to 6, what about the
    "outside" one?

    >>> x
    5

    It's still 5, since the 'x' inside the function was a local variable.
    """

    x += 1
    print(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
