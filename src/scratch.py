def x(point):
    return(point)
l = {'a':x,'b':x,'c':x}
ul = {}
for item in l:
    ul[item] = l[item](2)
print(ul) 
print(l)

print(isinstance(l['a'](2),float))
print(isinstance(l['a'](2),int))