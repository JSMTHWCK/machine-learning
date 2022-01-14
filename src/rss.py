from matrix import *
import gradient_descent 
import math 
def eq(a):
    return (a[2] -2) ** 2 + (a[0] + a[1] + a[2]) ** 2 + (4*a[0] + 2 * a[1] - 1 + a[2]) ** 2 + (9*a[0] + 3 * a[1] - 1 + a[2]) ** 2



def fit(coefficients, functions, original_eq = eq,step = 0.001,iteration = 10):
    copyfficients = list(coefficients)
    coefficients_the_second = coefficients
    for i in range(iteration):
        if i%1 == 0:
            print(original_eq(coefficients_the_second))
        data_points = coefficients_the_second
        for item in functions:
            coefficients_the_second[functions.index(item)] = coefficients_the_second[functions.index(item)] - step * item(coefficients)


        
    return coefficients

#def bonus(data_points, functions,step = 0.01,iteration = 1000):
    data_points_n = data_points.copy()
    for i in range(iteration):
        data_points = list(data_points_n)
        for item in functions:
            data_points_n[functions.index(item)] = data_points[functions.index(item)] - step * item(data_points)
        x = 0
        if i > 1:
            if roundarray(data_points_n,4) == roundarray(data_points,4):
                    print('only need {} attempts'.format(i))
                    return data_points_n
        
    return data_points_n

