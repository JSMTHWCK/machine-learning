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
        self.coefficients = coefficients.elements
        
    def predict(self, x):
        y = 0
        for i in range(self.n):
            y += self.coefficients[i][0] * (x ** i)
        return y

l = PolynomialRegressor()
data = [(1, 3), (2, 10), (3, 40), (4, 25), (5, 90), (6, 100), (7, 180), (8, 140), (9, 250), (10, 260)]
l.fit(data,8)
print(l.coefficients)
print(l.predict(3))