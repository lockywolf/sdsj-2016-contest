# coding=utf-8
u"""This file has a set of library functions for the basic FinMath exercise."""


class FinMath(object):
    u"""
    :FinMath This class is to learn finmath, time series analysis and stochastic PDEs."""
    pass  # Doesn't do anything, but reminds the syntax.

    def __init__(self):
        print("SdsjLibrary.py: mylibraryfunctionobject init: my name is " + __name__)

    @staticmethod
    def foo():

        return 2 + 3

    @property
    def return_true(self):
        return True


if __name__ == "__main__":
    print("I am from the sdsj package, but I am executed as a script and my name is: " + __name__)
