#!/usr/bin/python3
"""
Function to return a list of attributes or methods available
"""


def lookup(obj):
    """
    A function that returns the list of attributes of object/instance
    """
    return dir(obj)
