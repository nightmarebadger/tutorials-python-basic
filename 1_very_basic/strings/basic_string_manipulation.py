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

If you want to get a substring, you can use the same notation as in lists

>>> print(our_string[6:13])
ahaha t

As in lists, you can also specify the step - for instance if you want to turn
the whole string around, you could do

>>> print(our_string[::-1].strip())
asaspoh
alalart ahahah

There are also easy ways to check if a string starts or ends with a particular
substring

>>> our_string.endswith('hopsasa')
True
>>> our_string.startswith('hejho')
False

Another useful method (especially when comparing strings) is the .lower() one

>>> print("abCDEfgH".lower())
abcdefgh

Of course, .upper() also exists

>>> print(our_string.upper())
     HAHAHA TRALALA
HOPSASA

What if we have a list of some kind (for instance a list of names) and want to
join them into a nice string? We can use the .join() method. You call it on a
"separator" string and pass it a list, then the elements of the list get joined
together, separated by the "separator" string. The "separator" string can be
really simple or overly complex.

>>> names = ['Name1', 'Name2', 'Name3', 'Name4']
>>> print(''.join(names))
Name1Name2Name3Name4
>>> print(', '.join(names))
Name1, Name2, Name3, Name4
>>> print(' and his/her pal '.join(names))
Name1 and his/her pal Name2 and his/her pal Name3 and his/her pal Name4
"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
