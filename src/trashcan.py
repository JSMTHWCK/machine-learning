#predict for linearSandwich before realizing I messed up
def predict(self,values):
    total = 0 
    index = 0
    for a in range(0,len(values)):
        for b in range(0,len(values)):
            if a==b:
                total += self.coefficients[a] * values[a]
            elif b>a:
                total += self.coefficients[index] * values[a]*values[b]
            index += 1
    return total

