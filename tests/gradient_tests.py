import sys
import math

sys.path.append('src')
from matrix import roundarray

from gradient_descent import minimize, multivariable_minimize

def xsquared(x):
    return 2 * x

def x_test(x):
    return 2 * x + 9 * (x ** 2) + 4 * (x ** 3) + 3

def fpx(x):
    return 2 * x
def fpy(y):
    return 2 * (y-2)
def fpz(z):
    return 3 * (z-3)

def fpx2(x):
    return 2 * (x-1)
def fpy2(y):
    return 2 * (y-1)
def fpz2(z):
    return 3 * (z-1)


if round(minimize(xsquared,-12,0.91,10000),3) != 0:
    print("minimize failed on xsquared")
    print("wanted 0")
    print("got ",round(minimize(xsquared,-12,0.91,10000),3))

if round(minimize(x_test, 10, 0.001, 100000),2) != -2.18:
    print('minimize failed on x_test')
    print('wanted -2.18')
    print('got ',round(minimize(x_test,10,0.001,100000),2))
print('.')

if roundarray(multivariable_minimize([fpx,fpy,fpz],[1,1,1]) , 3) != [0.135,1.865,2.901]:
    print('multi descent failed')
    print('wanted [0.13,1.86,2.90]')
    print('got ',roundarray(multivariable_minimize([fpx,fpy,fpz],[1,1,1]),3))


if roundarray(multivariable_minimize([fpx2,fpy2,fpz2],[1,1,1]) , 3) != [1,1,1]:
    print('multi descent failed')
    print('wanted [1,1,1]')
    print('got ',roundarray(multivariable_minimize([fpx2,fpy2,fpz2],[1,1,1]),3))
print('.')