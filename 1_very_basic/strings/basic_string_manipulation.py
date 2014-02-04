r"""
    Some basic string manipulation. Since it's important to know exactly what
    goes on, all the code will be in a big doctest.


Let's create a simple string

>>> our_string = "     hahaha tralala\nhopsasa"
>>> print(our_string)
     hahaha tralala
hopsasa

Now let's say we wanted to get rid of the spaces at the beginning. We can do
this using the .strip() method, which strips whitespace from the left and right
side of the string, but keeps whitespace in the middle.

>>> print(our_string.strip())
hahaha tralala
hopsasa

We can also only strip from the left, or from the right using .rstrip(). If we
provide a parameter, we strip the provided characters instead of whitespace.

>>> print(our_string.rstrip('as'))
     hahaha tralala
hop

What about replacing some characters in a string? No problem, just use the
.replace() method.

>>> print(our_string.replace('a', 'A'))
     hAhAhA trAlAlA
hopsAsA

We can also replace multiple characters

>>> print(our_string.replace('     hahaha', 'heh'))
heh tralala
hopsasa

If we want to split our string into words, we can use the .split() method.

>>> our_string.split()
['hahaha', 'tralala', 'hopsasa']

By default it splits on whitespace, but we can also provide a parameter

>>> our_string.split('a')
['     h', 'h', 'h', ' tr', 'l', 'l', '\nhops', 's', '']

Of course multiple string manipulations together

>>> our_string.strip().replace('tral', 'gura').split()
['hahaha', 'guraala', 'hopsasa']

"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
