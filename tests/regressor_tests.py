import sys
sys.path.append('src')

import math
from linearRegressor import LinearRegressor
from analysis import LinearSandwich
from logisticRegressor import LogisticRegressor
from matrix import *

a = LogisticRegressor()
data = [[0,1],[1,1],[2,1]]
data2 = [[5,2],[8,11],[3,6]]
data3 = [[7,3],[11,5],[2,6]]
data4 = [[3,0.75],[2,0.5],[1,0.1]]

inttest = [[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [6, 0, 9], [0, 2, 2], [0, 4, 5], [0, 6, 7], [0, 8, 6], [2, 2, 1], [3, 4, 1]]
inttest2 = [[0,2,1],[3,0,2],[1,4,3],[2,3,4]]
a.fit (inttest,True)

print('hi')

if roundarray(a.coefficients,2) != [1.44,0.78,-0.66,0.94]:
	print("coefficients are incorrect")
elif math.isclose(a.predict([5,5]),-4.5478516025772615,abs_tol = 0.1) !=True:
	print("predict is wrong")
	print(a.predict([5,5]))
a.fit(inttest2,True)

if roundarray(a.coefficients,2) != [0.4,0.1,0.35,0.8]:
	print("a.coefficients are wrong")
elif math.isclose(a.predict([5,5]),12.050000000000063,abs_tol = 0.1) !=True:
	print("predict is wrong")
	a.predict([5,5])



'''
a.fit(data2)
if roundarray(a.coefficients,2) != [1.16,0.16]:
	print("coefficients are wrong at ",a.coefficients)
	print(a.coefficients)
elif math.isclose(a.predict([7]),8.25,abs_tol = 0.1)!= True:
	print("predict is wrong")
	print(a.predict([7]))

a.fit(data3)
if roundarray(a.coefficients,3) != [-0.131,5.541]:
	print("coefficients are wrong at ",a.coefficients)
elif math.isclose(a.predict([7]),4.62,abs_tol = 0.1)!= True:
	print("predict is wrong")
	print(a.predict([7]))

a.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6]])
if roundarray(a.coefficients,3) != [ 1.8, 0.675, 0.6]:
	print("linear fit failed at ",a.coefficients)

a.fit([[0, 0, 1], [1, 0, 2], [2, 0, 4], [4, 0, 8], [0, 8, 6], [0, 6, 7]])
if roundarray(a.coefficients,3) != [1.727, 0.785, 0.820]:
	print("linear fit failed at ", a.coefficients )
a = LogisticRegressor()
a.fit(data4)
if roundarray(a.coefficients,3) != [-1.648,3.662]:
	print("coefficients are wrong at ", a.coefficients)
elif math.isclose(a.predict([7]),7.07,abs_tol = 0.1):
	print("predict is wrong")

a.fit([[9, 0, 0.1], [1, 0, 0.2], [2, 0, 0.4], [4, 0, 0.8], [0, 8, 0.6]])
if roundarray(a.coefficients,3) != [ 0.158, -0.053, 0.017]:
	print("fit failed at ", a.coefficients)

a.fit([[11, 22, 0.3], [17, 1, 0.6], [0, 10, 0.2]])
if roundarray(a.coefficients,3) != [-0.087, 0.035, 1.038]:
	print("fit failed at ", a.coefficients)
'''