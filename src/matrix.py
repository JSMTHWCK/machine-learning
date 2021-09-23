class Matrix:

	def __init__(self,elements): # elements
		self.elements = elements
		self.numcols = len(self.elements[0])
		self.numrows = len(self.elements)
    #function    
	def print(self):
		
		for row in self.elements:
			print(row)
    #function    
	def transpose(self):

		final_array = []
		for a in range(0,len(self.numrows)):
			new_array = []
			for row in self.elements:
				new_array.append(row[a])
			final_array.append(new_array)
		return Matrix(final_array)
	#function
	def add(self, elements2):
		if self.numrows != elements2.numrows or self.numcols !=elements2.numcols:
			print("matricies are of unequal dimensions")
			return 
		final_array = []
		for i in range(0,self.numrows):
			new_array = []
			for a in range(0,self.numcols):
				new_array.append(self.elements[i][a] + elements2.elements[i][a])
			final_array.append(new_array)
		return Matrix(final_array)
	#function
	def scalar(self,scalar):

		final_array = []
		for row in self.elements:
			new_array = []
			for a in range(0,self.numcols):
				new_array.append(scalar * row[a])
			final_array.append(new_array)
		return Matrix(final_array)
	#helper
	def dot_product(self,vector1,vector2):
		x = 0
		for i in range(0,len(vector1)):
			x += vector1[i] * vector2[i]
		return x
	#helper
	def col_to_row(self,position):

		row = []
		for i in range(0,self.numrows):
			row.append(self.elements[i][position])
		return row
	#function
	def matrix_multiplication(self,matrix2):
		if self.numcols != matrix2.numrows:
			print("matricies are incompatable")

			return
		else: 
			print("it works")
		final_array = []
		for rowindex in range(0,self.numrows):
			new_array = []
			for colindex in range(0,matrix2.numcols):
				row = self.elements[rowindex]
				col = matrix2.col_to_row(colindex)
				#print("entry ", rowindex,colindex)
				#print("row " + str(row))
				#print("col " + str(col))
				dot_prod = self.dot_product(row,col)
				#print("dot " + str(dot_prod))
				#print('')
				new_array.append(dot_prod)
				#print(dot_prod)
				#print('')
				#print(new_array)
			final_array.append(new_array)
		return Matrix(final_array)
	
	def det(self):
		return self.elements[0][0] * self.elements[1][1] + self.elements[1][0] * self.elements[2][2]
		

a = Matrix([[3,10],[3,10]])
b = Matrix([[3,10],[0,2],[1,2]])
c = Matrix([[2,3],[1,2]])


#a.print()
a.add(c).print()
self.det(a)
b.matrix_multiplication(c).print()
