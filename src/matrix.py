

class Matrix:
	def __init__(self,vector): # elements
		self.vector = vector
		self.row = len(self.vector[0])
		self.column = len(self.vector)
        
	def print(self):
		for item in self.vector:
			print(item)
        
	def transpose(self):
		final_array = []
		for a in range(0,2):
			new_array = []
			for item in self.vector:
				new_array.append(item[a])
			final_array.append(new_array)
		return Matrix(final_array)

	def add(self, vector2):
		final_array = []
		for item in range(0,2):
			new_array = []
			for a in range(0,2):
				new_array.append(self.vector[item][a] + vector2[item][a])
			final_array.append(new_array)
		return Matrix(final_array)

	def scalar(self,scalar):
		final_array = []
		for item in self.vector:
			new_array = []
			for a in range(0,2):
				new_array.append(scalar *item[a])
			final_array.append(new_array)
		return Matrix(final_array)
'''
	def dot_product(self,vector1,vector2):
		return vector1[0] * vector2[0] + vector1[1] *vector2[1]
'''


				


        
        
a = Matrix([[1,2],[3,4]])
#a.print()

a.transpose().print()
a.scalar(3).print()
a.add([[1,2],[3,4]]).print()
