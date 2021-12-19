'''a = [{'a':1, 'b':2},{'a':2,'b':3},{'a':3, 'b':4}]
a[0] = a[1]
print(a)
'''

'''
stored_dict = []
for c in b:
    stored_dict.append(dict(zip(a,c)))
for d in stored_dict:
    print(d)
'''
a = [1,2,3,4,5]
b = [['a','b','c','d','e'],['b','c','d','e','f'],['c','d','e','f','g']]
c = []
for x in range(0,len(b[0])):
    array = []
    for y in range(0,len(b)):
        array.append(b[y][x])
    c.append(array)
data_dict = dict(zip(a,c))
print(data_dict)

#hi
