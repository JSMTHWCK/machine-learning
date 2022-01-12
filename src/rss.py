from matrix import *
import gradient_descent 

def fit(data_points, functions,step = 0.001,iteration = 1000):
    data_points_n = data_points
    for i in range(iteration):
        if i%1000 == 0:
            print(data_points)
        data_points = list(data_points_n)
        for item in functions:
            data_points_n[functions.index(item)] = data_points[functions.index(item)] - step * item(data_points)
        if data_points_n == data_points:
            return data_points
        
    return data_points_n

def bonus(data_points, functions,step = 0.01,iteration = 1000):
    data_points_n = data_points
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
