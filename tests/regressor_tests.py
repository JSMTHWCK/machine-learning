import sys
sys.path.append('src')

import math
from linearRegressor import LinearRegressor
from logisticRegressor import LogisticRegressor

a = LinearRegressor()

data = [[0,1],[1,1],[2,1]]
data2 = [[5,2],[8,11],[3,6]]
data3 = [[7,3],[11,5],[2,6]]
data4 =  [[12,5],[7,4],[12,5]]

a.fit(data2)
print(a.coefficients)
if math.isclose(a.coefficients[0],1.15,0.01 != True):
	continue
#if math.isclose(math.sqrt(3), rhapson(3,2,5), abs_tol = 0.00001) != True:
	#print('rhapson failed on input "3**1/2"')