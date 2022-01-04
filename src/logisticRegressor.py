from matrix import Matrix
import math


class LogisticRegressor():

	def fit(self, data,interaction_terms = False,min=1,max=2):
		self.min = min
		self.max = max
		print(self.min)
		print(self.max)
		x = [[self.max - point[-1]] for point in data]
		print(x)
		#right side
		right = [[math.log((self.max - point[-1])/(point[-1]-self.min))] for point in data]
		right = Matrix(right)
		#left side
		left = [point[:-1] for point in data]
		left_copy = left.copy()
		x = len(left_copy[0])
		for i in range(0,len(left)):
			#construction starts here
			if interaction_terms == True:
				for a in range(0,x):
					for b in range(0,x):
						if b>a:
							left[i].append(left[i][a] * left[i][b])
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
		total = 0
		copyfficients = self.coefficients.copy()
		for i in range(0,len(values)):
			total += self.coefficients[i] * values[i]
			copyfficients.pop(0)
		total +=  self.coefficients[-1]

		for a in range(0,len(values)):
			for b in range(0,len(values)):
				if b>a : 
					total += values[a] * values[b] * copyfficients[0]
					copyfficients.pop(0)
		return self.min + (self.max - self.min)/(1 + math.e ** (total))


