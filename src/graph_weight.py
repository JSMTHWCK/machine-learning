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
        return len(self.calc_shortest_path(start,end))
    
    def calc_shortest_path(self,start,end):
        priority = []
        self.nodes_by_id[str(start)].distance = 0
        a = 0
        while end not in priority:
            if len(priority) == 0:
                i = 1
                closest = start
            else:
                closest = priority[0]
            for child in self.get_children(closest):
                child_node = self.nodes_by_id[str(child)]
                child_node.shortest_parent = closest
                new_dist = int(self.nodes_by_id[str(child_node.shortest_parent)].distance) + int(self.weights[(child_node.shortest_parent,child_node.id)])
                if child_node.distance != new_dist:
                    print('h')
                    priority.append(child)
                if child_node.distance > new_dist:
                    child_node.distance = new_dist
            if i == 0:
                priority.pop(0)
            i = 0
            priority = self.sort_by_distance(priority)
            priority = self.remove_dupes(priority)
            while a < 10:
                print(priority)
                a += 1
        print(self.nodes_by_id[str(end)].distance)
        print('')

