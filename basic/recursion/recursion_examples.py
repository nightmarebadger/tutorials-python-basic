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


def fibonacci(n):
    """Find the n-th fibonacci number - the first two numbers are 1, the third
    one is the sum of the first two, the fourth one is the sum of the second
    and the third, ... meaning that fibonacci(n) = fibonacci(n-1) +
    fibonacci(n-2).

    This example also shows one of the possible problems with
    recursion - we calculate the same things over and over again! For instance,
    if we call fibonacci(5), we get a tree like this:

            5
       4         3
     3   2     2   1
    2 1

    As you can see, we called fibonacci(1) 2 times, fibonacci(2) 3 times and
    fibonacci(3) 2 times. Of course this can grow very fast, so if you call
    something like fibonacci(50), it can take a very long time to calculate the
    result.

    >>> [fibonacci(i) for i in range(1, 11)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """

    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


fibonacci_smarter_helper = {}


def fibonacci_smarter(n):
    """A smarter implementation of fibonacci - when we calculate a value, we
    save it inside the 'fibonacci_smarter_helper', so we do not have to
    calculate it again if (when) we need it again, we just get it from the
    helper.

    >>> [fibonacci_smarter(i) for i in range(1, 11)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> fibonacci_smarter(75)
    2111485077978050
    """

    if n <= 2:
        return 1

    # Get the solution from the helper (if it doesn't exist, we get None)
    solution = fibonacci_smarter_helper.get(n)

    # If the solution wasn't calculated yet, calculate it and save it in the
    # helper
    if not solution:
        solution = fibonacci_smarter(n-1) + fibonacci_smarter(n-2)
        fibonacci_smarter_helper[n] = solution

    return solution


if __name__ == "__main__":
    import doctest
    doctest.testmod()
