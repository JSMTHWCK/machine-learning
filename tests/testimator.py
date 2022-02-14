import sys
import math
sys.path.append('src')

from estimator import *
print("start")
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
def derivative(points):
    return 2 * points[0] + 1

l = EulerEstimate(derivative)
a = l.calc_estimated_points((0,0))

if a != [(0, 0), (0.5, 0.5), (1.0, 1.5), (1.5, 3.0), (2.0, 5.0)]:
    print('Euler Failed')
    print('wanted : [(0, 0), (0.5, 0.5), (1.0, 1.5), (1.5, 3.0), (2.0, 5.0)]')
    print('got : ',a)
print('finish')