import gradient_descent 

class Rss:
    def __init__(self,data_points, functions,step = 0.001,iteration = 1000):
        self.data_points = data_points 
        self.step = step
        self.iteration = iteration
        self.functions = functions
    
    def fit(self):
        return gradient_descent(self.functions,self.data_points,self.step,self.iteration)
        
        
        #distance formula

