from matrix import *
import gradient_descent 
import math 
def eq(a):
    return (a[2] -2) ** 2 + (a[0] + a[1] + a[2]) ** 2 + (4*a[0] + 2 * a[1] - 1 + a[2]) ** 2 + (9*a[0] + 3 * a[1] - 1 + a[2]) ** 2

def eqlog(l):
    a = l[0]
    b = l[1]
    return (1/(1 + math.e **(a * 0 + b)) - 0) **2 + (1/(1 + math.e **(a *  1+ b)) -0.5 ) **2 + (1/(1 + math.e **(a * 4 + b)) - 1) **2
def fit(coefficients, functions, original_eq = eq,step = 0.001,iteration = 1000):
    copyfficients = list(coefficients)
    coefficients_the_second = coefficients
    for i in range(iteration):
        if i%100 == 0:
            print(coefficients_the_second)
            print(original_eq(coefficients_the_second))
        data_points = coefficients_the_second
        for item in functions:
            coefficients_the_second[functions.index(item)] = coefficients_the_second[functions.index(item)] - step * item(coefficients)


        
    return coefficients


def bonus(data_points, functions,step = 0.0077,iteration = 1000):
    data_points_n = data_points
    for i in range(iteration):
        #if i<=100 and i >=90:
        #    print(i)
        #    print(eq(data_points))
        #if i%1000 == 0:
        #    print(eq(data_points))
        data_points = list(data_points_n)
        for item in functions:
            data_points_n[functions.index(item)] = data_points[functions.index(item)] - step * item(data_points)

        #if roundarray(data_points_n,3) == roundarray(data_points,3):
        if eq(data_points) < 0.8001:
            print('only took {} attempts'.format(i))
            return data_points_n
    return data_points
