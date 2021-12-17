import sys
sys.path.append('src')

from dataframe import *

data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

arr = [['Kevin', 'Fray', 5],
       ['Charles', 'Trapp', 17],
       ['Anna', 'Smith', 13],
       ['Sylvia', 'Mendez', 9]]


df1 = DataFrame(data_dict, ['John', 'Sarah', 'Pete'])
if df1.column_order != ['John', "Sarah", "Pete"]:
    print("column order failed ")
    print("wanted [John,Sarah,Pete]")
    print('got ',df1.column_order)
    
if df1.to_array() != [[2, 3, 1], [1, 1, 0], [0, 4, 1], [2, 0, 0]]:
    print("to_array doesn't work")
    print("wanted : [[2, 3, 1], [1, 1, 0], [0, 4, 1], [2, 0, 0]]")
    print('got ', df1.to_array())

df2 = df1.select_columns(['Sarah', 'Pete'])
if df2.to_array() != [[3, 1],[1, 0],[4, 1],[0, 0]]:
    print('select columns failed')
    print('wanted [[3, 1],[1, 0],[4, 1],[0, 0]]')
    print('got ', df2.to_array())
if df2.column_order != ['Sarah', 'Pete']:
    print('column order is wrong')
df3 = df1.select_rows([1,3])
df3.column_order = ['John','Sarah','Pete']
if df3.to_array() != [[1, 1, 0],[2, 0, 0]]:
    print('to array failed')
    print('wanted ',[[1, 1, 0], [2, 0, 0]])
    print('got ',df3.to_array())



df4 = DataFrame.from_array(arr, column_order=['firstname', 'lastname', 'age'])
df5 = DataFrame.from_json(df4.to_json(), ['firstname', 'lastname', 'age'])
if df4.to_array() != df5.to_array():
    print("from json or from array not working with to array")
if df4.data_dict == df5.data_dict:
    print('from json or to json not working with data dict ')



df6 = df5.order_by('lastname', ascending=False)
assert df6.to_array() == [['Charles', 'Trapp', 17], ['Anna', 'Smith', 13], ['Sylvia', 'Mendez', 9], ['Kevin', 'Fray', 5]]

assert df6.order_by('age', ascending=True).to_json() == [{'firstname': 'Kevin', 'lastname': 'Fray', 'age': 5}, {'firstname': 'Sylvia', 'lastname': 'Mendez', 'age': 9}, {'firstname': 'Anna', 'lastname': 'Smith', 'age': 13}, {'firstname': 'Charles', 'lastname': 'Trapp', 'age': 17}]