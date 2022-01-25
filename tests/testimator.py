from lib2to3.pygram import python_grammar
import sys
import math
sys.path.append('src')

from estimator import *
print("start")
'''<---------------------- SET 16 -------------------------->'''
#<------------------------ TEST 1 START -------------------->
def derivative(points):
    return points[0] + 1

l = EulerEstimate(derivative)
a = l.calc_estimated_points((1,4))

if a != [(1, 4), (1.5, 5.0), (2.0, 6.25), (2.5, 7.75), (3.0, 9.5)]:
    print('euler failed')
    print('wanted : [(1, 4), (1.5, 5.0), (2.0, 6.25), (2.5, 7.75), (3.0, 9.5)]')
    print('got : ', a)
#<------------------------ TEST 1 END -------------------->

#<------------------------ TEST 2 START -------------------->
def derivative(points):
    return 2 * points[0] + 1

l = EulerEstimate(derivative)
a = l.calc_estimated_points((0,0))
b = l.calc_estimated_points((0,0),'Range',[0,2],4)
if a != b:
    print('step -> range failed')
    print('step is ', a)
    print('range is ',b)
if a != [(0, 0), (0.5, 0.5), (1.0, 1.5), (1.5, 3.0), (2.0, 5.0)]:
    print('Euler Failed')
    print('wanted : [(0, 0), (0.5, 0.5), (1.0, 1.5), (1.5, 3.0), (2.0, 5.0)]')
    print('got : ',a)
#<------------------------ TEST 2 END -------------------->
'''<---------------------- SET 16 -------------------------->'''

'''<---------------------- SET 17 -------------------------->'''
def derivative(points):
    return 2 * points[0] - 2
l = EulerEstimate(derivative)
a = l.calc_estimated_points((0,-2),'Range',[0,5],5)
b = l.calc_estimated_points((0,-1),'Range',[0,5],5)
c = l.calc_estimated_points((0,0),'Range',[0,5],5)
d = l.calc_estimated_points((0,1),'Range',[0,5],5)
e = l.calc_estimated_points((0,2),'Range',[0,5],5)

print('(0,-2) gives ',a)
print('(0,-1) gives ',b)
print('(0,0) gives ',c)
print('(0,1) gives ',d)
print('(0,2) gives ',e)


def da_dt(t,state):
    return state['a'] + 1
def db_dt(t,state):
    return state['a'] + state['b']
def dc_dt(t,state):
    return 2 * state['b'] + 3 + t

derivatives = {'a':da_dt, 'b':db_dt, 'c':dc_dt}
    
'''<---------------------- SET 17 -------------------------->'''

print('finish')