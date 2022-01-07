import sys
sys.path.append('src')

from rss import *
from matrix import *


def b_one_grad(item):
    return ((10 * item[0]) + (6 * item[1]) - 18)

def a_one_grad(item):
    return ((26 * item[0]) + (10 * item[1]) - 42)

rss_one = fit([1,0], [a_one_grad, b_one_grad],0.001,1000000)

if roundarray(rss_one,4) != [1.2857,0.8571]:
    print('rss failed')
    print('wanted [1.2857,0.8571]')
    print('got ',rss_one)

print('hi')