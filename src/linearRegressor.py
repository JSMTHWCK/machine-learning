from matrix import Matrix

class LinearRegressor():

	def fit(self, data):
		rows = [[point[1]] for point in data]
		#left side
		y_matrix = Matrix(rows)
		print("the matrix of y is ", y_matrix.elements)
		#correct

		#right_copy
		m_b = [[point[0]] for point in data]
		for item in range(0,len(m_b)):
			m_b[item].append(1)
		data_matrix = Matrix(m_b)	
		
		print("the data of m and b are ",data_matrix.elements)
		#correct

		#tobetransposed
		transposed_data = data_matrix.transpose()
		print("the transposed data is ", transposed_data.elements)
		#correct

		#left side of equals
		left_side = transposed_data.matrix_multiplication(y_matrix)
		print("after multiplication, left side of = is ",left_side.elements)
		print("transposed data is ",transposed_data.elements)
		#right side of equals
		right_side = transposed_data.matrix_multiplication(data_matrix)
		print("after multiplication, right side of = is", right_side.elements)
		right_side = right_side.inverse()
		print("inverse is ", right_side.elements)
		print("left side is ",left_side.elements)
		right_side = right_side.matrix_multiplication(left_side)

		print("final is ",right_side.elements)
		
		self.coefficients = []
		for i in range(right_side.numrows):
			self.coefficients.append(right_side.elements[i][0])
		print('coefficients 1:', self.coefficients)

	def predict(self, x):
		
		return self.coefficients[0] * x + self.coefficients[1]

a = LinearRegressor()
data = [[0,1],[1,1],[2,2]]
data2 = [[3,6],[5,2],[8,11]]
a.fit(data2)
print(a.coefficients)
print(a.predict(7))