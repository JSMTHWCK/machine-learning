import copy
def mult_dict(dict,scale):
    dict_copy = copy.deepcopy(dict)
    for item in dict:
        dict_copy[item] = dict_copy[item]* scale
    return dict_copy
def add_dict(dict1, dict2):
    dict1_copy = copy.deepcopy(dict1)
    dict2_copy = copy.deepcopy(dict2)
    assert dict1.keys() == dict2.keys(), 'dicts have different keys'
    for item in dict1_copy:
        dict1_copy[item] += dict2_copy[item]
    return dict1_copy


class gen_estimator:
    def __init__(self,derivatives):
        self.derivatives = derivatives
    def calc_derivatives_at_point(self,initial_point):
        answer = {}
        for l in self.derivatives.keys():
            answer[l] = self.derivatives[l](initial_point[0],initial_point[1])
        return answer

    def calc_estimated_points(self,point,step_size=2,num_steps = 3):
        fin = [point]
        state = point[0]
        fun = point[1]
        keys = fun.keys()
        for i in range(1,num_steps+1):
            new_point = [state + step_size * i]
            new_point.append(add_dict(fin[-1][1],mult_dict(self.calc_derivatives_at_point(fin[-1]),step_size)))
            fin.append(tuple(new_point))
        return fin