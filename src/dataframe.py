class DataFrame:
    def __init__(self,data_dict,column_order = ['Pete', 'John', 'Sarah']):
        self.data_dict =  data_dict 
        self.column_order = column_order
        self.values = list(data_dict.values())
    def to_array(self):
        for a in range(0,len(self.values[0])):
            new_array = []
            for row in self.values:
                new_array.append(row[a])
            print(new_array)
        
data_dict = {
    'Pete': [1, 0, 1, 0],
    'John': [2, 1, 0, 2],
    'Sarah': [3, 1, 4, 0]
}

df1 = DataFrame(data_dict)
print(df1.column_order)
print(df1.data_dict)
print(df1.values)
df1.to_array()