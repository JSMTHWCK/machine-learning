from matrix import Matrix

class linearSandwich():
	def fit(self, data,interaction_terms=False):
		n = len(data[0])
		rows = [[point[n-1]] for point in data]

		y_matrix = Matrix(rows)



		m_b = [point[0:n-1] for point in data]
		for item in range(0,len(m_b)):
			if interaction_terms == True:
				m_b[item].append(m_b[item][0] *m_b[item][1])
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

	def predict(self,values):
		total = 0
		if len(values) + 1 != len(self.coefficients):
			print("number of variables aren't consistant")
			return
		for i in range(0,len(values)):
			total += self.coefficients[i] * values[i]
		total +=  self.coefficients[-1]
		return total



a = linearSandwich()
data_0 = [[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]]
data = [[0,0,1],[1,0,2],[2,0,4],[4,0,8],[6,0,9],[0,2,2],[0,4,5],[0,6,7],[0,8,6],[2,2,1],[3,4,1]]
a.fit(data_0)

sandwich = open("./tests/hotdog_test.txt","w")
sandwich.write("input of [5,0] gives {} \n".format(a.predict([5,0])))
sandwich.write("input of [5,5] gives {} \n".format(a.predict([5,5])))