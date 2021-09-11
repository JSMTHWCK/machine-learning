class Matrix:
	def __init__(self,vector):
		self.vector = vector
		self.row = len(vector)
		self.column = len(vector[0])


	def print(self):
		for item in self.vector:
			print(item)
	
	def transpose(self):
		for a in range(0,2):
			new_array = []
			for item in self.vector:
				new_array.append(item[a])
			print(new_array)	



a = Matrix([[1,2],[3,4]])
a.print()
a.transpose()