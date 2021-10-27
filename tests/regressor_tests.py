import sys
sys.path.append('src')

import math
from linearRegressor import LinearRegressor
from logisticRegressor import LogisticRegressor
from matrix import *

a = LinearRegressor()

data = [[0,1],[1,1],[2,1]]
data2 = [[5,2],[8,11],[3,6]]
data3 = [[7,3],[11,5],[2,6]]
data4 =  [[12,5],[7,4],[12,5]]

a.fit(data2)
if roundarray(a.coefficients,2) != [1.16,0.16]:
	print("coefficients are wrong at ",a.coefficients)
	print(a.coefficients)
elif math.isclose(a.predict(7),8.25,abs_tol = 0.1)!= True:
	print("predict is wrong")
	print(a.predict(7))
#if math.isclose(math.sqrt(3), rhapson(3,2,5), abs_tol = 0.00001) != True:
	#print('rhapson failed on input "3**1/2"')