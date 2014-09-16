# -*- coding: utf-8 -*-

"""
An example of using properties in a class:
    http://docs.python.org/2/library/functions.html#property

Properties have many use-cases, for instance when we want to have a class
attribute that is limited to a specific value or type, but don't want to set it
using methods like .setX() or something similar.
"""


class Person(object):

    """An example Person class. You can set the name and age, with the age
    being limited to non-negative integers.

    Let's try to create a Person with an impossible age

    >>> Person("Peter", -10)
    Traceback (most recent call last):
    ...
    Exception: Age must be a non-negative integer!

    Now let's try again with something viable

    >>> peter = Person("Peter", 10)

    Now, we *could* use the functions we wrote:

    >>> peter.getAge()
    10
    >>> peter.setAge(11)
    >>> peter.getAge()
    11

    But it's nicer and easier to use the property we defined:

    >>> peter.age
    11
    >>> peter.age = 12
    >>> peter.age
    12

    Of course, we still can't set it to something that's not possible:

    >>> peter.age = 12.5
    Traceback (most recent call last):
    ...
    Exception: Age must be a non-negative integer!
    >>> peter.age
    12

    What we could do (if we needed to) is cheat a bit and bypass the function,
    changing the "internal" variable directly (it is not actually internal or
    protected in any way, we just use _ in front of names to make sure people
    know variables like this are meant to be used by the program in the
    background and probably have different ways to set them up somewhere).

    >>> peter._age = 'Blablabla'
    >>> peter.age
    'Blablabla'

    Of course we usually don't want that, so let's set it back to something
    viable ... oh and happy birthday Peter :)

    >>> peter.age = 13
    >>> peter.age
    13
    """

    def __init__(self, name, age):
        self.name = name
        self.setAge(age)

    def getAge(self):
        """The "getter", it gets the age and returns it."""
        return self._age

    def setAge(self, age):
        """The "setter", it sets the age that is passed to if it is in the
        format we wanted. If there is something wrong, raise an Exception."""

        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            raise Exception("Age must be a non-negative integer!")

    age = property(fget=getAge, fset=setAge)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
