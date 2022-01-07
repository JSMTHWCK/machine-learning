import gradient_descent 

def fit(data_points, functions,step = 0.001,iteration = 1000):
    data_points_n = data_points
    x = 0
    for i in range(iteration):
        data_points = list(data_points_n)
        for item in functions:
            data_points_n[functions.index(item)] = data_points[functions.index(item)] - step * item(data_points)
        if data_points_n == data_points:
            return data_points
        
    return data_points_n

