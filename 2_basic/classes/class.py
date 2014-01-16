# -*- coding: utf-8 -*-

"""
    A class creation and usage example.
"""


class Person(object):
    """Create an example Person class that can introduce himself or herself.

    >>> anna = Person("Anna", "Smith", 22)
    >>> anna.say_hello()
    Hello, I am Anna Smith and I am 22 years old!

    """

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def say_hello(self):
        """Introduces himself or herself"""

        print("Hello, I am {0} {1} and I am {2} years old!".format(
            self.name,
            self.surname,
            self.age)
        )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
