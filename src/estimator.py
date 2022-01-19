class EulerEstimate:
    def __init__(self,derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self,point):
        return self.derivative(point)

    def calc_estimated_points(self,point,step_size = 0.5, num_steps = 4,full_graph = False):
        #https://mathacademy.com/topics/eulers-method:-calculating-one-step-602#step-13
        self.point = list(point)
        fin = []
        x = [self.point[0]]
        y = [self.point[1]]
        yprime = [self.calc_derivative_at_point(self.point)]
        deltay = [step_size * yprime[0]]
        #pre append x
        for i in range(1,num_steps+1):
            x.append(x[0] + step_size*i)
            y.append(y[i-1] + deltay[i-1])
            yprime.append(self.calc_derivative_at_point([x[i]]))
            deltay.append(step_size * yprime[i])
        #print(x)
        #print(y)
        #print('')
        #print(yprime)
        #print(deltay)
        for item in range(len(x)):
            fin.append(tuple([x[item],y[item]]))
        #print('')
        #print(fin)
        return fin
        





