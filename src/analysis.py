from matrix import Matrix

class LinearSandwich():

	def fit(self, data,interaction_terms = False):

		self.coefficients = []

		rows = [[point[-1]] for point in data]

		y_matrix = Matrix(rows)

		m_b = [point[0:-1] for point in data]
		m_b_copy = m_b
		x = len(m_b_copy[0])
		for item in range(0,len(m_b)):
			#construction starts here
			if interaction_terms == True:
				for a in range(0,x):
					for b in range(0,x):
						if b>a:
							m_b[item].append(m_b[item][a] * m_b[item][b])
				#construction ends here
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

#elias your names are something else
pain = [[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6]]
data = [[0,0,1],[1,0,2],[2,0,4],[4,0,8],[6,0,9],[0,2,2],[0,4,5],[0,6,7],[0,8,6],[2,2,1],[3,4,1]]
a = LinearSandwich()

a.fit(data,True)
print(a.coefficients)
doc = open("../tests/hotdog_test.txt", "w")
doc.write("5 rb + 0 pb =  " + str(a.predict([5, 0])) + "\n")
doc.write("5 rb + 5 pb =  " + str(a.predict([5, 5])))