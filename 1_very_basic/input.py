# -*- coding: utf-8 -*-

"""
    How to get input from the user. Note that this is Python 2.7, the Python 3+
    version is in the "input3.py" file.
"""

# Get an integer from the user (will error on non-number)
x = int(input("Write an integer: "))
print(x)

# Get a float (will error on non-number)
y = float(input("Write a float: "))
print(y)

# Get a string
z = raw_input("Write something: ")
print(z)
