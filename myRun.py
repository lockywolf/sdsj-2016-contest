# coding=utf-8
u""" Default run file.
"""
from avellaneda2008 import library
# import avellaneda2008


def mymain():
    """
    Mymain is the main function, protected from being executed at import.
    """
    print('myrun.py: my name is ' + __name__)
    myobject = library.FinMath()
    pass


if __name__ == '__main__':
    mymain()
