
class Matrix:

	def __init__(self,elements): # elements
		self.elements = elements
		self.numcols = len(self.elements[0])
		self.numrows = len(self.elements)
    
	#helper in general
	def copy(self):
		copied_matrix = [[element for element in row] for row in self.elements]
		return Matrix(copied_matrix)

	#helper in general
	def dot_product(self,vector1,vector2):
		x = 0
		for i in range(0,len(vector1)):
			x += vector1[i] * vector2[i]
		return x
	#helper in general
	def col_to_row(self,position):

		row = []
		for i in range(0,self.numrows):
			row.append(self.elements[i][position])
		return row	

	#helper in general
	def det(self):
		return self.elements[0][0] * self.elements[1][1] - self.elements[1][0] * self.elements[0][1]
	#helper in general
	def sub_matrix(self, column):
		matrix_copy = self.copy().elements
		del matrix_copy[0]
		for row in matrix_copy:
			del matrix_copy[matrix_copy.index(row)][column]
		return Matrix(matrix_copy)



	#helper for current assignment
	def rowswitch(self,a,b):
		row_switched = self.copy().elements
		#print("switching ",row_switched)
		#print("The rows {} and {} are switching.".format(a,b))
		#print("before was ", row_switched)
		row_switched[a],row_switched[b] = row_switched[b],row_switched[a]
		#print("now is ", row_switched)
		return Matrix(row_switched)
	#helper for current assignment
	def rowadd(self,a,b,scalar):
		row_added = self.copy().elements
		#print("a is {}, b is {}, and scalar is {}".format(row_added[a],row_added[b],scalar))
		empty_array =[]
		for i in range(0,self.numcols):
			x = row_added[a][i] = row_added[a][i] + scalar*row_added[b][i]
			empty_array.append(x)
		#print("before was ", row_added[a])
		row_added[a] = empty_array
		#print("now is", row_added[a])
		return Matrix(row_added)
	#helper for current assignment
	def rowscale(self,a,scalar):
		scale_copy = self.copy().elements
		#rint("{} is being scaled by {}".format(a,scalar))
		row_scaled = self.copy().elements
		for i in range(0,self.numcols):
			row_scaled[a][i] = row_scaled[a][i] * scalar
		scale_copy[a] = row_scaled[a]
		#print("after scaling, it is now ",scale_copy)
		return Matrix(scale_copy)

	#helper for current assignment
	#not finished yet
	def getfirstpivot(self,i):
		for a in range(0, self.numcols):
			if a <= i:
				if self.elements[a][i] != 0:
					if self.elements[a][:i]	== [0] * len(self.elements[a][:i]):
						return a
		return i
	#helper for current assignment
	def roundmatrix(self,accuracy):
		round_copy = self.copy().elements
		for a in range(0,self.numrows):
			for b in range(0,self.numcols):
				round_copy[a][b] = round(round_copy[a][b],accuracy)		
		return Matrix(round_copy)

	def augment(self,matrix2):
		#print("original matrix is ", self.elements)
		augmented_matrix = self.copy().elements
		for item in range(0,self.numcols):
			for a in range(0,len(augmented_matrix)):
				#print(item)
				#print(a)
				augmented_matrix[item].append(matrix2.elements[item][a])
				#print(augmented_matrix[item])
		return Matrix(augmented_matrix)
	def unaugment(self):
		unaugmented_matrix = self.copy().elements
		for item in range(0,self.numrows):
			unaugmented_matrix[item] = unaugmented_matrix[item][self.numrows:]
		return Matrix(unaugmented_matrix)
	#function
	def identitymatrix(self):
		identity = []
		for a in range(0,self.numrows):
			identity.append([])
			for b in range(0,self.numcols):
				if a == b:
					identity[a].append(1)
				else:
					identity[a].append(0)
		return Matrix(identity)
			
	def print(self):
		
		for row in self.elements:
			print(row)


	def scalar(self,scalar):

		final_array = []
		for row in self.elements:
			new_array = []
			for a in range(0,self.numcols):
				new_array.append(scalar * row[a])
			final_array.append(new_array)
		return Matrix(final_array)
		    #function    
	def transpose(self):
		final_array = []
		for a in range(0,self.numcols):
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
	def matrix_multiplication(self,matrix2):
		if self.numcols != matrix2.numrows:
			print("matricies are incompatable")

			return
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
	

	def recursive_det(self):
		if self.numcols != self.numrows:
			#print("cannot take a determinant")
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
	def rref(self):
		matrix_copy = self.copy()
		for i in range(0,matrix_copy.numrows):
			#print("we are on {}th passthrough".format(i))
			if i >= self.numcols:
				#print("reached end of matrix")
				return matrix_copy
			#print(i)
			#print(self.numcols)
			matrix_copy = matrix_copy.rowswitch(i,self.getfirstpivot(i))
			#print("after running swap helper, matrix copy is now ", matrix_copy.elements)
			#need to find way to find pivot, just assume first is pivot right now 
			matrix_copy = matrix_copy.rowscale(i,1/matrix_copy.elements[i][i])
			#print("after running scale helper, matrix_copy is now ", matrix_copy.elements)			
			for a in range(0,matrix_copy.numrows):
				#print("")
				if a == i:
					continue
				else:
					matrix_copy = matrix_copy.rowadd(a,i,-1 * matrix_copy.elements[a][i])
					#last left here
			#print("after clear, matrix copy is", matrix_copy.elements)
			#print("")

		return matrix_copy
	def determinant(self):
		if self.numrows != self.numcols:
			return 0
		scalars = []
		rowswaps = []
		matrix_copy = self.copy()
		for i in range(0,matrix_copy.numrows):
			if i >= self.numcols:
				return matrix_copy
			if matrix_copy.elements != matrix_copy.rowswitch(i,self.getfirstpivot(i)).elements:
				rowswaps.append(1)
			matrix_copy = matrix_copy.rowswitch(i,self.getfirstpivot(i))
			scalars.append(matrix_copy.elements[i][i])
			matrix_copy = matrix_copy.rowscale(i,1/matrix_copy.elements[i][i])
			for a in range(0,matrix_copy.numrows):
				if a == i:
					continue
				else:
					matrix_copy = matrix_copy.rowadd(a,i,-1 * matrix_copy.elements[a][i])

		final = 1
		for item in scalars:
			final = final * item
		final = (-1)**len(rowswaps) * final
		return final

	def inverse(self):
		if self.numcols != self.numrows or self.det() == 0:
			print("unable to compute ",self.elements)
			return
		matrix_copy = self.copy()
		identity = self.identitymatrix()
		matrix_copy = matrix_copy.augment(identity)
		matrix_copy = matrix_copy.rref()
		matrix_copy = matrix_copy.unaugment()
		#print(matrix_copy.elements)
		return matrix_copy

def roundarray(input,accuracy):
	for a in range(0,len(input)):
		input[a] = round(input[a],accuracy)
	return input

a = Matrix([[3,10],[3,10]])
b = Matrix([[3,10,11],[0,2,3],[1,2,3]])
c = Matrix([[2,3],[1,2]])
d = Matrix([[5,10,2,12],[2,10,10,7],[7,6,11,12],[4,2,11,15]])
e = Matrix([[3,10,11,14],[0,2,3,3],[1,2,3,3]])
f = Matrix([[2,3,2],[1,3,4],[1,5,6],[7,4,4]])
#a.print()
#a.add(c).print()
#print(a.det())
'''
print(d.recursive_det())
b.matrix_multiplication(c).print()
print("hi")
d.switch(0,2).print()
a.scalar(3).print()
print("")
b.rowadd(0,1,1).print()
b.rowscale(0,3).print()
print("")
'''
