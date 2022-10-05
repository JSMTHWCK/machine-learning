import math

class Node:
    def __init__(self,id):
        self.id = id
        self.distance = math.inf
        self.shortest_parent = None
    
#using idea from https://www.youtube.com/watch?v=EFg3u_E6eHU&list=TLPQMjQwNDIwMjL-K2JAUm8tGg&index=2    
class WeightedGraph:
    def __init__(self,values):
        self.edges = list(values.keys())
        self.weights = values
        self.parents = [edge[0] for edge in self.edges]
        self.children = [edge[1] for edge in self.edges]
        self.nodes_by_id = {}
        
        for i in self.parents:
            self.nodes_by_id[str(i)] = Node(i)
        for i in self.children:
            if str(i) not in self.nodes_by_id:
                self.nodes_by_id[str(i)] = Node(i)
    def reset_nodes_by_id(self):
        for i in self.parents:
            self.nodes_by_id[str(i)] = Node(i)
        for i in self.children:
            if str(i) not in self.nodes_by_id:
                self.nodes_by_id[str(i)] = Node(i)
    def get_children(self,value):
        empty_array = []
        for i in range(0,len(self.parents)):
            if self.parents[i] == value:
                empty_array.append(self.children[i])
        return empty_array
    
    def get_parents(self,value):
        empty_array = []
        for i in range(0,len(self.children)):
            if self.children[i] == value:
                empty_array.append(self.parents[i])
        return empty_array
    
    def sort_by_distance(self,array):
        node = self.nodes_by_id
        for n in array:
            for i in range(len(array)):
                if i > 0:
                    while node[str(array[i])].distance < node[str(array[i-1])].distance:
                        array[i],array[i-1] = array[i-1],array[i]
        return array
    def remove_dupes(self,array):
        unique = []
        for i in array:
            if i not in unique:
                unique.append(i)
        return unique
    def calc_distance(self,start,end):
        a = self.calc_shortest_path(start,end)
        return self.nodes_by_id[str(a[-1])].distance

    def calc_shortest_path(self,start,end):
        self.reset_nodes_by_id()
        priority = [start]
        visited = {start:True}
        self.nodes_by_id[str(start)].distance = 0
        while priority[0] != end: #while you haven't reached the end point
            for child in self.get_children(priority[0]):
                chld_nd = self.nodes_by_id[str(child)]
                if chld_nd.shortest_parent == None:
                    chld_nd.shortest_parent = priority[0]
                priority.append(child)
                #print(priority)
                poss_dist = self.weights[(priority[0],child)] + self.nodes_by_id[str(priority[0])].distance
                if poss_dist < chld_nd.distance:
                    chld_nd.shortest_parent = priority[0]
                    chld_nd.distance = poss_dist
            visited[priority[0]] = True
            for i in visited:
                if i in priority:
                    priority.remove(i)
            self.sort_by_distance(priority)
        order = [end]

        while start not in order:
            order.append(self.nodes_by_id[str(order[-1])].shortest_parent)
        order.reverse()
        return order
                
