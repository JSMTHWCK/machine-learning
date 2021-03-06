class DataFrame:
    def __init__(self,data_dict,column_order = ['Pete', 'John', 'Sarah']):
        self.data_dict =  data_dict
        self.column_order = column_order
        self.values = list(data_dict.values())



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
        return cls(data_dict,column_order = column_order)

    def order_by(self,col,ascending = True):
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
        if ascending == False:
            for item in range(0,len(list(self.data_dict.values()))):
                list(self.data_dict.values())[item].reverse()


    def to_json(self):
        dicts = [{} for i in list(self.data_dict.values())[0]]
        for i in range(0,len(dicts)):
            for values in self.column_order:
                dicts[i][values] = self.data_dict[values][i]

        return dicts


    @classmethod
    def from_json(cls, json, column_order):

        dict = {}
        for a in range(0, len(column_order)):
            column = column_order[a]
            dict[column] = []
            for i in range(0, len(json)):
                dict[column].append(json[i][column])
        return cls(dict, column_order=column_order)
