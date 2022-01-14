import sys
sys.path.append('src')

from rss import *
from matrix import *
print('started')
# <-------------------- Linear Start -------------------->
def b_one_grad(item):
    return ((10 * item[0]) + (6 * item[1]) - 18)

def a_one_grad(item):
    return ((26 * item[0]) + (10 * item[1]) - 42)

#rssl_one = fit([1,0], [a_one_grad, b_one_grad],0.001,1000000)

#if roundarray(rssl_one,4) != [1.2857,0.8571]:
#    print('rss failed')
#    print('wanted [1.2857,0.8571]')
#    print('got ',rssl_one)
# <-------------------- Linear End -------------------->

# <-------------------- Non-Linear Start -------------------->

def a_one_grad_pb(item): 
    return ((196 * item[0]) + (72 * item[1]) + (28 * item[2]) -26)

def b_one_grad_pb(item): 
    return ((72 * item[0]) + (28 * item[1]) + (12 * item[2]) -10)

def c_one_grad_pb(item): 
    return ((28 * item[0]) + (12 * item[1]) + (8 * item[2]) - 8)
rssp = fit([1,0,0],[a_one_grad_pb, b_one_grad_pb, c_one_grad_pb],eq, 0.0001, 10)
if roundarray(rssp,4) != [0.499,-1.6965,1.7982]:
    print('rssp failed')
    print('wanted [0.499,-1.6965,1.792]')
    print('got ',roundarray(rssp,4))
# <-------------------- Non-Linear End -------------------->

print('finished')