# -*- coding: utf-8 -*-

"""
An example using some of the Python special class methods.
    http://docs.python.org/2/reference/datamodel.html#basic-customization
"""

from __future__ import division


def gcd(a, b):
    """Return the greatest common divisor of a and b.

    >>> gcd(2, 10)
    2
    >>> gcd(6, 9)
    3
    >>> gcd(5, 22)
    1
    """

    if a % b == 0:
        return b

    return gcd(b, a % b)


class Fraction(object):

    """A simple fraction."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """A representation that can be used to directly build the same
        Fraction.

        >>> Fraction(5, 12)
        Fraction(5, 12)
        >>> Fraction(2, -3)
        Fraction(2, -3)
        """

        return "Fraction({0}, {1})".format(self.x, self.y)

    def __str__(self):
        """A user-friendly representation of the Fraction.

        >>> print(Fraction(2, 4))
        2/4
        >>> print(Fraction(-2, 4))
        -2/4
        >>> print(Fraction(2, -4))
        -2/4
        >>> print(Fraction(-2, -4))
        2/4
        """

        sign = ''

        if (self.x < 0 and not self.y < 0) or (self.y < 0 and not self.x < 0):
            sign = '-'

        return "{0}{1}/{2}".format(sign, abs(self.x), abs(self.y))

    def value(self):
        """Returns the value of the Fraction.

        >>> Fraction(1, 2).value()
        0.5
        >>> Fraction(2, 4).value()
        0.5
        """

        return self.x / self.y

    def __lt__(self, oth):
        """Less then; x < y.

        >>> Fraction(1, 2) < Fraction(1, 3)
        False
        >>> Fraction(1, 2) < Fraction(1, 2)
        False
        >>> Fraction(-2, 5) < Fraction(2, 3)
        True
        """

        return self.value() < oth.value()

    def __le__(self, oth):
        """Less or equal then; x <= y.

        >>> Fraction(1, 2) <= Fraction(1, 3)
        False
        >>> Fraction(1, 2) <= Fraction(1, 2)
        True
        >>> Fraction(-2, 5) <= Fraction(2, 3)
        True
        """

        return self.value() <= oth.value()

    def __gt__(self, oth):
        """Greater then; x > y.

        >>> Fraction(1, 2) > Fraction(1, 3)
        True
        >>> Fraction(1, 2) > Fraction(1, 2)
        False
        >>> Fraction(-2, 5) > Fraction(2, 3)
        False
        """

        return self.value() > oth.value()

    def __ge__(self, oth):
        """Greater or equal then; x >= y.

        >>> Fraction(1, 2) >= Fraction(1, 3)
        True
        >>> Fraction(1, 2) >= Fraction(1, 2)
        True
        >>> Fraction(-2, 5) >= Fraction(2, 3)
        False
        """

        return self.value() >= oth.value()

    def __eq__(self, oth):
        """Equal; x == y.

        >>> Fraction(1, 2) == Fraction(1, 3)
        False
        >>> Fraction(1, 2) == Fraction(1, 2)
        True
        >>> Fraction(-2, 5) == Fraction(2, 3)
        False
        >>> Fraction(1, 2) == Fraction(2, 4)
        True
        """

        return self.value() == oth.value()

    def __ne__(self, oth):
        """Not equal; x != y.

        >>> Fraction(1, 2) != Fraction(1, 3)
        True
        >>> Fraction(1, 2) != Fraction(1, 2)
        False
        >>> Fraction(-2, 5) != Fraction(2, 3)
        True
        >>> Fraction(1, 2) != Fraction(2, 4)
        False
        """

        return self.value() != oth.value()

    def __mul__(self, oth):
        """Multiplication of two Fractions.

        >>> print(Fraction(1, 2) * Fraction(2, 5))
        1/5
        >>> print(Fraction(1, 2) * Fraction(2, -5))
        -1/5
        >>> print(Fraction(-1, 2) * Fraction(1, -2))
        1/4
        """

        result = Fraction(self.x * oth.x, self.y * oth.y)
        result.reduce()
        return result

    def __div__(self, oth):
        """Division of two Fractions.

        >>> print(Fraction(1, 2) / Fraction(2, 10))
        5/2
        >>> print(Fraction(1, 2) / Fraction(2, -5))
        -5/4
        >>> print(Fraction(-3, 5) / Fraction(7, -9))
        27/35
        """

        result = Fraction(self.x * oth.y, self.y * oth.x)
        result.reduce()
        return result

    def __truediv__(self, oth):
        """True division, used when importing division from __future__ etc."""

        return self.__div__(oth)

    def __add__(self, oth):
        """Addition of two Fractions.

        >>> print(Fraction(1, 2) + Fraction(1, 2))
        1/1
        >>> print(Fraction(3, 5) + Fraction(1, 10))
        7/10
        """

        x = self.x * oth.y + oth.x * self.y
        y = self.y * oth.y
        result = Fraction(x, y)
        result.reduce()
        return result

    def __sub__(self, oth):
        """Substraction of two Fractions.

        >>> print(Fraction(2, 3) - Fraction(1, 3))
        1/3
        >>> print(Fraction(8, 6) - Fraction(2, 3))
        2/3
        """

        x = self.x * oth.y - oth.x * self.y
        y = self.y * oth.y
        result = Fraction(x, y)
        result.reduce()
        return result

    def reduce(self):
        """Reduce the fraction.

        >>> frac = Fraction(2, 4)
        >>> frac.reduce()
        >>> print(frac)
        1/2

        >>> frac = Fraction(5, 8)
        >>> frac.reduce()
        >>> print(frac)
        5/8

        >>> frac = Fraction(-6, 9)
        >>> frac.reduce()
        >>> print(frac)
        -2/3
        """

        divisor = gcd(self.x, self.y)
        self.x //= divisor
        self.y //= divisor


if __name__ == "__main__":
    import doctest
    doctest.testmod()
