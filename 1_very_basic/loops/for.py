# -*- coding: utf-8 -*-

"""
Created on 2014-09-16
:author: Natan Žabkar (nightmarebadger)

A for loop is usually used when we want to repeat a piece of code 'n' number of
times, or when we want to iterate through the elements of a list (or something
similar).

In this example our program will 'sing' out the 99 bottles of beer song
(http://en.wikipedia.org/wiki/99_Bottles_of_Beer). We use .format() to put the
number of bottles in the text and we use an if sentance for the last two
verses.
"""

for i in range(100):
    bottle_num = 99 - i
    song = """{0} bottles of beer on the wall, {0} bottles of beer.
Take one down, pass it around, {1} bottles of beer on the wall ...
"""
    song_one = """1 bottle of beer on the wall, 1 bottle of beer.
Take it down, pass it around, there are no bottles left on the wall ...
"""
    song_no = """No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy us some more, 99 bottles of beer on the wall ...
"""
    if i == 99:
        print(song_no)
    elif i == 98:
        print(song_one)
    else:
        print(song.format(bottle_num, bottle_num - 1))
