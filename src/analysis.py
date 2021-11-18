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
		index = 0
		for a in range(1,len(values)):
			for b in range(1,len(values)):
				if a==b:
					total += self.coefficients[a] * values[a]
				elif b>a:
					total += self.coefficients[index] * values[a]*values[b]
				index += 1
		total += self.coefficients[0]
		
		return total


a = linearSandwich()
data = [[0,0,1],[1,0,2],[2,0,4],[4,0,8],[6,0,9],[0,2,2],[0,4,5],[0,6,7],[0,8,6],[2,2,1],[3,4,1]]
a.fit(data)
print(a.coefficients)
print(a.predict([5,0]))
print(a.predict([5,5]))

#the problem? we don't have data on a mixture, so when predicting a mixture, it would most likely be wrong.