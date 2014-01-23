# -*- coding: utf-8 -*-

"""
    An example on how to write to a file. Keep in mind that the paths for
    opening the file are relative, so you need to run this from inside the
    'files' folder to work properly.
"""


def writeToFile(filename, text):
    """Write to the file named 'filename'.

    We will something and add the current date and time to the end so the file
    changes on each call.

    >>> from datetime import datetime
    >>> date = datetime.now()
    >>> writeToFile('writing.txt', "Testing a file write. {0}".format(date))

    It should be written now, let's test it by opening the file and printing
    everything. We will ignore the date in the test since I can't find a way to
    make it work properly right now :)

    >>> with open('writing.txt') as f:
    ...     print(f.read()) # doctest: +ELLIPSIS
    Testing a file write. ...
    """

    with open(filename, 'w') as f:
        f.write(text)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
