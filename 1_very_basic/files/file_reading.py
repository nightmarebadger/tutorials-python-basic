# -*- coding: utf-8 -*-

"""
    An example on how to read from a file. Keep in mind that the paths for
    opening the file are relative, so you need to run this file from inside the
    folder it is located in for the tests to work.
"""


def readFile(filename):
    """Read the file named 'filename' and print the whole thing.

    >>> readFile("reading.txt")
    I've paid my dues
    Time after time
    I've done my sentence
    But committed no crime
    And bad mistakes
    I've made a few
    I've had my share of sand
    Kicked in my face
    But I've come through
    <BLANKLINE>
    And we mean to go on and on and on and on
    <BLANKLINE>
    We are the champions - my friends
    And we'll keep on fighting
    Till the end
    We are the champions
    We are the champions
    No time for losers
    'Cause we are the champions of the World
    <BLANKLINE>
    """

    with open(filename) as f:
        print(f.read())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
