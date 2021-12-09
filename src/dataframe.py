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
    def select_rows(self,rows):
        new_array = []
        a = self.to_array()
        for item in rows:
            new_array.append(a[item])
    @classmethod
    def from_array(cls,arr,column_order = ["firstname","lastname","age"]):

        stored_dict = []
        for x in range(0,len(arr[0])):
            array = []
            for y in range(0,len(arr)):
                array.append(arr[y][x])
            stored_dict.append(array)
        data_dict = dict(zip(column_order,stored_dict))
        return data_dict

        
data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

arr = [['Kevin', 'Fray' , 5],['Charles', 'Trapp', 17],['Anna', 'Smith', 13],['Sylvia', 'Mendez', 9]]

df1 = DataFrame(data_dict)
print(df1.data_dict)
print(df1.column_order)
print(df1.to_array())
df2 = df1.select_columns(["John", "Sarah"])
print(df2.to_array())
df3 = DataFrame.from_array(arr)
print(df3)
