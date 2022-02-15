class gen_estimator:
    def __init__(self,derivatives):
        self.derivatives = derivatives
        self.dimensions = [key for key in derivatives]
    def calc_derivatives_at_point(self,initial_point):
        answer = {}
        for l in self.derivatives.keys():
            answer[l] = self.derivatives[l](initial_point[0],initial_point[1])
        return answer
    def calc_estimated_points(self,point,step_size=2,num_steps = 3):
        self.point = point
        fin = []
        #basically x
        t = [self.point[0]]
        for i in range(num_steps):
            t.append(self.point[0] + step_size * i)
        print(t)
        #basically y
        state = [self.point[1]]
        state_prime = [self.calc_derivatives_at_point(self.point[1])]
        delta_state = []
        #combining things together
        for item in range(len(t)):
            fin.append(tuple([t[item],state[item]]))
        return fin
