import sys
sys.path.append('src')

from rss import *
from matrix import *

def a_one_grad_pb(item): 
    return ((196 * item[0]) + (72 * item[1]) + (28 * item[2]) -26)
def b_one_grad_pb(item): 
    return ((72 * item[0]) + (28 * item[1]) + (12 * item[2]) -10)
def c_one_grad_pb(item): 
    return ((28 * item[0]) + (12 * item[1]) + (8 * item[2]) - 8)
#rssp = bonus([1,0,0],[a_one_grad_pb, b_one_grad_pb, c_one_grad_pb], 0.0066, 1000000)
#rrsp = fit([1,0,0],[a_one_grad_pb, b_one_grad_pb, c_one_grad_pb], 0.0001, 1000000)

#print('r is ',rssp)
