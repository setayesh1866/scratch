import sys

from . import pages


def page_0():
    p = {
        '0': sys.exit, 
        '1': page_1,
        '2': page_2,
    }
    print(pages.page_0)
    replay = input('replay: ')
    print("################")
    p[replay]()

def page_1():
    p = {
        '0': page_0, 
    }
    print(pages.page_1)
    replay = input('replay: ')
    print("################")
    p[replay]()

def page_2():
    pass
