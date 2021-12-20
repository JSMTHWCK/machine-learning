import sys
import math
sys.path.append('src')

from gradient_descent import minimize

def xsquared(x):
    return 2 * x

def x_test(x):
    return 2 * x + 9 * (x ** 2) + 4 * (x ** 3) + 3

if round(minimize(xsquared,-12,0.91,10000),3) != 0:
    print("minimize failed on xsquared")
    print("wanted 0")
    print("got ",round(minimize(xsquared,-12,0.91,10000),3))

if round(minimize(x_test, 10, 0.001, 100000),2) != -2.18:
    print('minimize failed on x_test')
    print('wanted -2.18')
    print('got ',round(minimize(x_test,10,0.001,100000),2))
print('.')
