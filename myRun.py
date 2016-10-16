# coding=utf-8
u""" Default run file.
"""
from sdsj import library
# import sdsj


def mymain():
    """
    Mymain is the main function, protected from being executed at import.
    """
    print('myrun.py: my name is ' + __name__)
    myobject = library.FinMath()
    pass


if __name__ == '__main__':
    mymain()
