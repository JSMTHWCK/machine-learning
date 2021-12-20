def minimize(prime,x,step,iterations):
    while iterations > 0:
        iterations -= 1
        x = x - step * prime(x)
    return x

def xsquared(x):
    return 2 * x
