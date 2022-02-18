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
        self.dimensions = [key for key in derivatives]
    def calc_derivatives_at_point(self,initial_point):
        answer = {}
        for l in self.derivatives.keys():
            answer[l] = self.derivatives[l](initial_point[0],initial_point[1])
        return answer

    def calc_estimated_points(self,point,step_size=2,num_steps = 3):
        fin = []
        state = [point[0]]
        function = [copy.deepcopy(point[1])]
        function_prime = [self.calc_derivatives_at_point(point)]
        delta_function = [mult_dict(function_prime[0],step_size)]

        for i in range(1,num_steps + 1):
            #so far so good
            state.append(state[0] + step_size * i)
            function.append(add_dict(function[i-1],delta_function[i-1]))
            #breaks here
            function_prime.append(self.calc_derivatives_at_point([state[-1],function[-1]]))
            delta_function.append(mult_dict(function_prime[-2],step_size))

            print('state is ', state)
            print('')
            print('function is ', function)
            print('')
            print('function prime is ', function_prime)
            print()
            print('delta_function is ', delta_function)
            print()
        for item in range(len(state)):
            fin.append(tuple([state[item],function[item]]))
        return fin

