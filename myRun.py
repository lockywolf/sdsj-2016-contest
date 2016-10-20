# coding=utf-8
u""" Default run file.
"""
import csv

from sdsj import SdsjLibrary

try:
    # noinspection PyCompatibility
    from StringIO import StringIO
except ImportError:
    from io import StringIO
# import sdsj


def mymain():
    """
    Mymain is the main function, protected from being executed at import.
    """
    print('myrun.py: my name is ' + __name__)
    myobject = SdsjLibrary.FinMath()
    mycustid_stat= dict()
    with open('transactions.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0.0
        for row in reader:
            i += 1.0
            print(i/7000000.0, "% complete \n")
            if row['customer_id'] in mycustid_stat:
                mycustid_stat[row['customer_id']] += 1
            else:
                mycustid_stat[row['customer_id']] = 1

    pass


if __name__ == '__main__':
    mymain()
