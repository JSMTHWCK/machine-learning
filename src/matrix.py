class Matrix:

	def __init__(self,elements): # elements
		self.elements = elements
		self.column = len(self.elements[0])
		self.row = len(self.elements)
        
	def print(self):

		for item in self.elements:
			print(item)
        
	def transpose(self):

		final_array = []
		for a in range(0,2):
			new_array = []
			for item in self.elements:
				new_array.append(item[a])
			final_array.append(new_array)
		return Matrix(final_array)

	def add(self, elements2):
		if self.row != len(elements2) or self.column !=len(elements2[0]):
			print("matricies are of unequal dimensions")
			return
		final_array = []
		for item in range(0,2):
			new_array = []
			for a in range(0,2):
				new_array.append(self.elements[item][a] + elements2[item][a])
			final_array.append(new_array)
		return Matrix(final_array)

	def scalar(self,scalar):

		final_array = []
		for item in self.elements:
			new_array = []
			for a in range(0,2):
				new_array.append(scalar * item[a])
			final_array.append(new_array)
		return Matrix(final_array)

	def dot_product(self,vector1,vector2):

		return vector1[0] * vector2[0] + vector1[1] * vector2[1]

	def col_to_row(self,matrix,position):

		row = []
		for item in range(0,2):
			row.append(matrix[item][position])
		return row
	
	def matrix_multiplication(self,matrix2):

		final_array = []
		for row in range(0,2):
			new_array = []
			for column in range(0,2):
				dot_prod = self.dot_product(self.elements[row],self.col_to_row(matrix2,column))
				new_array.append(dot_prod)
			final_array.append(new_array)
		return Matrix(final_array)



a = Matrix([[1,2],[3,4]])
#a.print()
a.add([[3,10,24],[24,13,5]])
