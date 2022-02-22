from matrix import Matrix, roundarray

class PolynomialRegressor:
    def fit(self,points,n):
        self.n = n
        #converting tuples into list
        for i in range(0,len(points)):
            points[i] = list(points[i])
        y_matrix = [[point[-1]] for point in points]
        y_matrix_class = Matrix(y_matrix)
        eq_matrix = [[] for a in points]
        for i in range(0,len(eq_matrix)):
            for item in range(self.n):
                eq_matrix[i].append(points[i][0]**item)
        eq_matrix_class = Matrix(eq_matrix)
        eq_transpose = eq_matrix_class.transpose()
        y_matrix_class = eq_transpose.matrix_multiplication(y_matrix_class)
        eq_matrix_class = eq_transpose.matrix_multiplication(eq_matrix_class)
        coefficients = eq_matrix_class.inverse().matrix_multiplication(y_matrix_class)
        self.coefficients = coefficients.roundmatrix(3).elements
        
        
        

l = PolynomialRegressor()
l.fit([(1,2),(3,4),(5,6)],3)
print(l.coefficients)