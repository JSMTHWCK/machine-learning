from matrix import Matrix 
def isolate(arr,equation_index,item_index):
    mat = Matrix(arr)
    fm_element = mat.elements
    #first reduce down equation line
    mat = mat.rowscale(equation_index,1/fm_element[equation_index][item_index])
    fm_element = mat.elements
    for i in range(0,len(mat.elements)):
        if i != equation_index:
            mat = (mat.rowadd(i,equation_index,-1 * fm_element[i][item_index]))
    return mat.elements

def simplex(arr):
    while True:
        #if everything is negative or zero
        if max(arr[0][0:-1]) <= 0:
            for line in arr:
                print(line)
            return -1 * arr[0][-1]
        else:
            for line in arr:
                print(line)
            print("new max is ",arr[0][-1]*-1)
            #print(arr)
            print('')
        high_slope = arr[0].index(max(arr[0][0:-1]))
        #gets value of all indexes
        constraints = [row[-1]/row[high_slope] for row in arr[1:]]
        #finds highest constraint (+1 since ignoring top)
        #something right here is probably wrong
        constraints = [abs(element) for element in constraints]
        high_constraint = constraints.index(min(constraints)) + 1
        #clear all
        arr = isolate(arr,high_constraint,high_slope)
        





#print(simplex([[1,2,1,0,0,0,0],[2,1,1,1,0,0,14],[4,2,3,0,1,0,28],[2,5,5,0,0,1,30]]))
print(simplex([[20,10,15,0,0,0,0,0],[3,2,5,1,0,0,0,55],[2,1,1,0,1,0,0,26],[1,1,3,0,0,1,0,30],[5,2,4,0,0,0,1,57]]))