import sys
sys.path.append('src')

import math
from linearRegressor import LinearRegressor
from analysis import LinearSandwich
from logisticRegressor import LogisticRegressor
from matrix import *



logistic_regressor = LogisticRegressor()
test_data = [[0, 0, 1], [2, 2, 1], [6, 0, 9], [0, 6, 7]]

logistic_regressor.fit(test_data, True, 0, 10)
coefficients = logistic_regressor.coefficients

if roundarray(coefficients,3) != [-0.732,-0.507,0.620,2.197]:
	print('logistic failed')
	print('wanted [2.197,-0.732,-0.507,0.620]')
	print('got ',roundarray(coefficients,3))
print('2')
if round(logistic_regressor.predict([0, 6]),2) != 7.0:
	print('predict failed')
	print('wanted 7')
	print('got ',round(logistic_regressor.predict([0, 6]),2))

print('print statements are just checkpoints')
'''
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

