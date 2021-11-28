x = 5
list = []
for a in range(0,x):
	for b in range(0,x):
		if b > a:
			list.append(str(a) + str(b))


print(list)