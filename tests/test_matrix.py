import sys
import math
sys.path.append('src')

from matrix import Matrix

#a.print()


a = Matrix([[9,24,16,30,21,13,26,7,5,29],[22,13,20,28,14,30,16,26,20,17],[25,3,15,11,3,9,10,18,11,11],[25,6,30,8,15,15,1,23,9,15],[27,5,11,25,19,25,8,29,2,30],[17,12,26,27,25,17,28,21,14,4],[30,20,26,17,28,19,7,17,30,7],[5,19,5,2,4,27,19,20,8,23],[14,9,15,20,11,6,1,12,15,14],[6,7,23,2,13,28,30,12,1,11]])
b = Matrix([[14,8,3,3,14],[7,7,21,5,8],[22,18,3,10,22],[24,11,5,18,11],[21,19,25,14,7]])
c = Matrix([[20,6,24,23,14],[25,7,22,13,4],[15,4,4,18,17],[8,25,9,14,19],[6,11,1,22,10]])
d = Matrix([[2,22,7,1,5],[15,20,5,19,4],[17,8,24,23,13],[3,13,5,4,1],[6,19,19,6,17]])

a.determinant() #the magnificant 10x10
if math.isclose(b.determinant(),323555,abs_tol = 1) != True:
    print("determinant failed on ", b.elements)
    print(b.determinant())
if math.isclose(c.determinant(),1643549,abs_tol = 0.01) != True:
    print("determinant failed on ", c.elements)
if math.isclose(d.determinant(),-21545,abs_tol = 0.01) != True:
    print("determinant failed on ", d.elements)
