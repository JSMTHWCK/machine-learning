from matrix import Matrix
import math


class LogisticRegressor():

	def fit(self, data):
		#right side
		right = [[math.log(1/point[-1] - 1)] for point in data]
		right = Matrix(right)
		#left side
		left = [point[:-1] for point in data]

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
		for i in range(right_side.numrows):
			self.coefficients.append(right_side.elements[i][0])


	def predict(self,values):
		powertotal = 0
		if len(values) + 1 != len(self.coefficients):
			print("number of variables aren't consistant")
			return
		for i in range(0,len(values)):
			powertotal += self.coefficients[i] * values[i]
		powertotal +=  self.coefficients[-1]
		return 1/(1 + math.e ** (powertotal))


a = LogisticRegressor()
data = [[0,1],[1,1],[2,1]]
data2 = [[3,0.75],[2,0.5],[1,0.1]]
a.fit(data2)