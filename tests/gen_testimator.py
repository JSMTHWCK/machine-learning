import sys
import math
sys.path.append('src')

from estimator import *
from gen_estimator_take_2 import *

'''<--------------------Part A) start ----------------------->'''
def derivative(points):
    return points[0] - 2 

'''
l = EulerEstimate(derivative)
a = l.calc_estimated_points((0,-2))
print(a)
a = l.calc_estimated_points((0,-1))
print(a)
a = l.calc_estimated_points((0,0))
print(a)
a = l.calc_estimated_points((0,1))
print(a)
a = l.calc_estimated_points((0,2))
print(a)
'''
#here it is in desmos, need to convert to pandas
#https://www.desmos.com/calculator/h4obt56s4u
'''<--------------------Part A) end ----------------------->'''

'''<--------------------Part B) start----------------------->'''
initial_state = {'a': -0.45, 'b': -0.05, 'c': 0}
initial_point = (-0.4, initial_state)
# points are now of the form (t, state)

def da_dt(t, state):
        return state['a'] + 1
def db_dt(t, state):
        return state['a'] + state['b']
def dc_dt(t, state):
        return 2 * state['b'] + 3 * t
derivatives = {
    'a': da_dt,
    'b': db_dt,
    'c': dc_dt
}
    
l = gen_estimator(derivatives)
print(l.calc_derivatives_at_point(initial_point))
print(l.calc_estimated_points(initial_point , step_size =2,  num_steps =3))