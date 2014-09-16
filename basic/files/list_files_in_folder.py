# -*- coding: utf-8 -*-

"""
An example on how to list all files and folders inside a directory. Keep in
mind that the paths are relative, so you need to run this file from inside the
folder it is located in for the tests to work.
"""

from os import getcwd
from os import listdir
from os.path import isfile
from os.path import join


def list_files_and_folders(folder=''):
    """Lists files and folders in the (relative) folder by the name 'folder'.
    If you don't specify a folder, it is called on the current directory.

    >>> list_files_and_folders('example_folder')
    a.txt
    b.txt
    c.txt
    folder
    """

    # Get the current path
    current_path = getcwd()
    # And add the folder we got to it
    current_path = join(current_path, folder)

    # List all items inside the path
    for f in listdir(current_path):
        print(f)


def list_files_only(folder=''):
    """Lists only files in the (relative) folder by the name 'folder'. If you
    don't specify a folder, it is called on the current directory.

    >>> list_files_only('example_folder')
    a.txt
    b.txt
    c.txt
    """

    # Get the current path
    current_path = getcwd()
    # And add the folder we got to it
    current_path = join(current_path, folder)

    # List all items inside the path
    for f in listdir(current_path):
        # If the item is a file, print it's name. We need to put the whole
        # (absolute) path for the check, so we need to join the current path
        # with the filename to get the results.
        if isfile(join(current_path, f)):
            print(f)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
