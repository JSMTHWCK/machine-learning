from matrix import Matrix

class LinearRegressor():

	def fit(self, data):
		n = len(data[0])
		rows = [[point[n-1]] for point in data]

		y_matrix = Matrix(rows)

		m_b = [point[0:n-1] for point in data]
		for item in range(0,len(m_b)):
			m_b[item].append(1)
		data_matrix = Matrix(m_b)	
		transposed_data = data_matrix.transpose()
		left_side = transposed_data.matrix_multiplication(y_matrix)
		right_side = transposed_data.matrix_multiplication(data_matrix)
		right_side = right_side.inverse()
		right_side = right_side.matrix_multiplication(left_side)
		for i in range(right_side.numrows):
			self.coefficients.append(right_side.elements[i][0])

	def predict(self,values):
		total = 0
		for i in range(0,len(values)):
			total += self.coefficients[i] * values[i]
		total +=  self.coefficients[-1]
		return total

