class Matrix:

	def __init__(self,elements): # elements
		self.elements = elements
		self.numcols = len(self.elements[0])
		self.numrows = len(self.elements)
    
	#helper (copies matrix into non matrix)
	def copy(self):
		copied_matrix = [[element for element in row] for row in self.elements]
		return Matrix(copied_matrix)
	
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
		return self.elements[0][0] * self.elements[1][1] - self.elements[1][0] * self.elements[0][1]
	
	def sub_matrix(self, column):
		matrix_copy = self.copy().elements
		del matrix_copy[0]
		for row in matrix_copy:
			del matrix_copy[matrix_copy.index(row)][column]
		return Matrix(matrix_copy)

	def recursive_det(self):
		if self.numcols != self.numrows:
			print("cannot take a determinant")
			return
		
		elif self.numrows == 2 and self.numcols == 2:
			return self.det()
			
		
		else:
			determinant = 0
			#print("works 1")
			for i in range(0, self.numcols):
				coefficient = self.elements[0][i] * ((-1) ** i)
				smaller_matrix = self.sub_matrix(i)
				cofactor = coefficient * smaller_matrix.recursive_det()
				determinant += cofactor
				#print("works 2")
			return determinant
			

a = Matrix([[3,10],[3,10]])
b = Matrix([[3,10],[0,2],[1,2]])
c = Matrix([[2,3],[1,2]])
d = Matrix([[5,10,2,12],[2,10,10,7],[7,6,11,12],[4,2,11,15]])

#a.print()
#a.add(c).print()
#print(a.det())
print(d.recursive_det())

#b.matrix_multiplication(c).print()
