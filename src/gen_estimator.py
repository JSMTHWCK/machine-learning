class gen_estimator:
    def __init__(self,derivatives):
        self.derivatives = derivatives
    def calc_derivatives_at_point(self,initial_point):
        answer = {}
        for l in self.derivatives.keys():
            answer[l] = self.derivatives[l](initial_point[0],initial_point[1])
        return answer


