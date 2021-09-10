class Matrix:
	def __init__(self,vector):
		self.vector = vector
		self.row = len(vector)
		self.column = len(vector[0])


	def print(self):
		for item in self.vector:
			print(item)

a = Matrix([[1,2],[3,4]])
a.print()