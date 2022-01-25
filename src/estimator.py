class EulerEstimate:
    def __init__(self,derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self,point):
        if isinstance(point,float) or isinstance(point,int):
            return self.derivative(point)
        else:
            returnpoint = {}
            for item in point:
                returnpoint[item] = self.derivative[item](point)
            return returnpoint

    def calc_estimated_points(self,point,mode = 'Step',step_size = 0.5, num_steps = 4,):
        #https://mathacademy.com/topics/eulers-method:-calculating-one-step-602#step-13
        if mode == 'Range':
            step_size = (step_size[1] - step_size[0])/num_steps
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

        for item in range(len(x)):
            fin.append(tuple([x[item],y[item]]))

        return fin
        





