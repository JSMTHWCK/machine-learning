def minimize(prime,x,step,iterations):
    while iterations > 0:
        iterations -= 1
        x = x - step * prime(x)
    return x

def multivariable_minimize(functions,initial_points,step = 0.001,iteration=1000):
    for i in range(0,iteration):
        for i in range(0,len(functions)):
            prime = functions[i](initial_points[i])
            initial_points[i] -= step * prime 
    return initial_points
def xsquared(x):
    return 2 * x
