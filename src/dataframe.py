class DataFrame:
    def __init__(self,data_dict,column_order = ['Pete', 'John', 'Sarah']):
        self.data_dict =  data_dict 
        self.column_order = column_order
        self.values = list(data_dict.values())

    def to_array(self):
        final_array = [[] for row in range(0,len(self.values) + 1)]
        for a in range(0,len(final_array)):
            for b in range(0,len(self.column_order)):
                final_array[a].append(self.values[b][a])
        return final_array

    def select_columns(self,columns):
        dict_copy = {}
        for col in columns:
            dict_copy[col] = self.data_dict[col]
        return DataFrame(dict_copy, column_order = columns)
        
    def to_array(self):
        array = [[] for i in range(len(self.data_dict[self.column_order[0]]))]
        for values in self.column_order: 
            for i in range(len(array)):
                array[i].append(self.data_dict[values][i])
        return array 


    def select_rows(self,rows):
        new_array = []
        a = self.to_array()
        for item in rows:
            new_array.append(a[item])

        return DataFrame.from_array(new_array, column_order = self.column_order)
    @classmethod
    def from_array(cls,arr,column_order = ["firstname","lastname","age"]):

        stored_dict = []
        for x in range(0,len(arr[0])):
            array = []
            for y in range(0,len(arr)):
                array.append(arr[y][x])
            stored_dict.append(array)
        data_dict = dict(zip(column_order,stored_dict))
        return cls(data_dict)
    
    def order_by(self,col,ascending = False):
        if col not in list(self.data_dict):
            print('{} is not a value'.format(str(col)))
            return 
        i = list(self.data_dict).index(col)
        index_array = []
        x= 0

        for item in range(0,len(list(self.data_dict.values())[0])):
            index_array.append(x)
            x = x+1

        #----------------------------------> Card sort <---------------------------------#
        for n in list(self.data_dict.values())[i]:
            for item in range(0, len(list(self.data_dict.values())[i])):
                if item > 0:
                    while list(self.data_dict.values())[i][item] < list(self.data_dict.values())[i][item - 1]:
                        list(self.data_dict.values())[i][item], list(self.data_dict.values())[i][item - 1] = list(self.data_dict.values())[i][item - 1], list(self.data_dict.values())[i][item]
                        index_array[item], index_array[item-1] =   index_array[item-1], index_array[item]
        for sub_index in range(0,len(list(self.data_dict.values()))):
            index_copy = index_array.copy()
            if sub_index == i:
                    continue
            else:
                for item in range(0,len(index_copy)):
                    index_copy[item],index_copy[index_copy.index(item)] = index_copy[index_copy.index(item)],index_copy[item]
                    list(self.data_dict.values())[sub_index][item],list(self.data_dict.values())[sub_index][index_copy.index(item)] = list(self.data_dict.values())[sub_index][index_copy.index(item)],list(self.data_dict.values())[sub_index][item]
        if ascending == True:
            for item in range(0,len(list(self.data_dict.values()))):
                list(self.data_dict.values())[item].reverse()
    
    def to_json(self): 
        dicts = [{} for i in range(0, len(self.data_dict) + 1)]
        print('hi')
        print(self.column_order)


    @classmethod
    def from_json(cls,json, column_order):
        json = {}
        for item in column_order: 
            dict[item] = []
            for i in range(0,len(json)):
                dict[values].append(json[i][item])
        return cls(json, column_order = column_order)

    

            


