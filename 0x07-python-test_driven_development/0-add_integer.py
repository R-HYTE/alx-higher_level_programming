#!/usr/bin/python3

def add_integer(a, b=98):
    """ Addition of 2 Integers """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        a = int(a)
        b = int(b)
        return a + b
    else:
        message = " must be an integer"
        if type(a) not in [int, float]:
            raise TypeError("a" + message)
        elif type(b) not in [int, float]:
            raise TypeError("b" + message)
