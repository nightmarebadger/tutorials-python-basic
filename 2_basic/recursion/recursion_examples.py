# -*- coding: utf-8 -*-

"""
    A function is recursive when it calls itself (on a smaller piece of the
    problem). We need to provide a 'stopping criterion' or else the function
    will call itself indefinitely (therefore hanging the program).
        http://en.wikipedia.org/wiki/Recursion_(computer_science)

    You can find some simple examples of recursion below, but recursion will
    also be used in other examples (for instance in some sorting algorithms).
"""


def factorial(n):
    """A factorial of n (n!) is defined as the product of all positive integers
    less then or equal to n. According to the convention for an empty product,
    the value of factorial(0) (0!) is 1.

    >>> [factorial(i) for i in range(11)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    """

    # The stopping criterion is when we reach 1 or less
    if n <= 1:
        return 1
    # n! = n * (n-1) * (n-2) * ... * 2 * 1, therefore
    # n! = n * (n-1)!
    return n * factorial(n-1)


def gcd(a, b):
    """Find the greatest common divisor using Euclid's algorithm.

    >>> gcd(1, 3)
    1
    >>> gcd(2, 10)
    2
    >>> gcd(6, 9)
    3
    >>> gcd(17, 289)
    17
    >>> gcd(2512561, 152351)
    1
    """

    if a % b == 0:
        return b
    return gcd(b, a % b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
