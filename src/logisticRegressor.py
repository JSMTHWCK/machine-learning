from matrix import Matrix
import math


class LogisticRegressor():

	def fit(self, data):
		#right side
		right = [[math.log(1/point[1] - 1)] for point in data]
		right = Matrix(right)
		#left side
		left = [[point[0]] for point in data]

		for i in range(0,len(left)):
			left[i].append(1)
		left = Matrix(left)
		transposed = left.transpose()
		
		#print("left is ",left.elements)
		#print("right is ",right.elements)
		#print("transposed is ",transposed.elements)
		left_side = transposed.matrix_multiplication(left)
		right_side = transposed.matrix_multiplication(right)
		left_side = left_side.inverse()
		right_side = left_side.matrix_multiplication(right_side)
		#print(right_side.elements)
		self.coefficients = []
		self.coefficients.append(right_side.elements[1][0])
		self.coefficients.append(right_side.elements[0][0])
	def predict(self,x):
		return 1/(1 + math.e ** ((self.coefficients[1] * x) + self.coefficients[0]))


a = LogisticRegressor()
data = [[0,1],[1,1],[2,1]]
data2 = [[3,0.75],[2,0.5],[1,0.1]]

