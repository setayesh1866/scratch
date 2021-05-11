import sys

import page

se = "series2, series3, series5, series6(it call GT too) ,series7"
x = "X1, X3, X4, X5, X6, X7"
m = "M2 competition, M5 competition, M760Li, Z4 M40i, M8 Coupe, X5 copetition, X7 M50d"
z = "Z4 rodster"
def fi_0():
    p = {
        '0': sys.exit, 
        '1': page.fi_1,
        '2': page.fi_2,
        '3': page.fi_3,
        '4': page.fi_4,
    }
    print(apge.fi_0)
    replay = input('replay: ')
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    p[replay]()

def fi_0():
    p = {
        '0': sys.exit, 
        '1': se,
        '2': x,
        '3': m,
        '4': z,
    }
    print(page.fi_1)
    replay = input('replay: ')
    print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
    p[replay]()

fi_0()