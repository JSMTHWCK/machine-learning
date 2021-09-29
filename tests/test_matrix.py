import sys
sys.path.append('src')

from matrix import Matrix

a = Matrix([[1,2],[3,4]])
#a.print()

a.transpose().print()
a.scalar(3).print()
a.add([[1,2],[3,4]]).print()
a.matrix_multiplication([[1,2],[3,4]])

