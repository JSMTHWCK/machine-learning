from matrix import Matrix

class linearSandwich():
#just copied from linearRegressor
	def fit(self, data):
		rows = [[point[1]] for point in data]
		y_matrix = Matrix(rows)
		m_b = [[point[0]] for point in data]
		for item in range(0,len(m_b)):
			m_b[item].append(1)
		data_matrix = Matrix(m_b)	
		transposed_data = data_matrix.transpose()
		left_side = transposed_data.matrix_multiplication(y_matrix)
		right_side = transposed_data.matrix_multiplication(data_matrix)
		right_side = right_side.inverse()
		right_side = right_side.matrix_multiplication(left_side)		
		self.coefficients = []
		for i in range(right_side.numrows):
			self.coefficients.append(right_side.elements[i][0])

	def predict(self, x):
	
		return self.coefficients[0] * x + self.coefficients[1]

