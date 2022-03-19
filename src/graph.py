from audioop import reverse


class Node:
	def __init__(self,id):
		self.id = id
		self.distance = 0

class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.parents = [edge[0]  for edge in edges]
		self.children = [edge[1] for edge in edges]
		self.nodes_by_id = {}

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
	def bfs(self):
		queue = [self.parents[0]]
		visited = {}
		order = []

		while len(queue) != 0:
			item = queue[0]
			if str(item) not in visited:
				visited[str(item)] = True
				order.append(item)
				for children in self.get_children(queue[0]):
					queue.append(children)
			queue.pop(0)

		return order

	def dfs(self):
		queue = [self.parents[0]]
		visited = {}
		order = []

		while len(queue) != 0:
			item = queue[0]
			queue.pop(0)
			if str(item) not in visited:
				visited[str(item)] = True
				order.append(item)
				for a in self.get_children(item):
					queue.insert(0,a)

		return order


	def set_distance_and_previous(self,start_index):
		'''<---- BFS START ---->'''
		self.nodes_by_id = {}
		queue = [start_index]
		visited = {}
		order = []
		self.nodes_by_id[str(queue[0])] = Node(queue[0])
		while len(queue) != 0:
			item = queue[0]
			if str(item) not in visited:
				visited[str(item)] = True
				order.append(item)
				for children in self.get_children(queue[0]):
					queue.append(children)
					if str(children) not in visited:
						self.nodes_by_id[str(children)] = Node(children)
						self.nodes_by_id[str(children)].distance = self.nodes_by_id[str(item)].distance + 1
			queue.pop(0)
	def calc_distance(self,start_index,end_index):
		self.set_distance_and_previous(start_index)
		if str(end_index) not in self.nodes_by_id:
			return False
		else:
			return self.nodes_by_id[str(end_index)].distance

	def calc_shortest_path(self,start_index,end_index):
		reverse_order = [end_index]
		self.set_distance_and_previous(start_index)
		if str(end_index) not in self.nodes_by_id:
			return False
		while reverse_order[-1] != start_index:
			a = self.get_parents(reverse_order[-1])
			x = 0
			for item in a:
				if str(item) not in self.nodes_by_id:
					continue
				elif self.nodes_by_id[str(item)].distance == self.nodes_by_id[str(reverse_order[-1])].distance - 1:
					if x != 1:
						reverse_order.append(item)
					x = 1
		return reverse_order[::-1]
		

graph = Graph([[2,8],[9,3],[1,5],[9,6],[9,6],[6,9],[4,5],[10,6],[3,10],[8,7],[8,5],[6,2],[8,10],[6,1],[6,4]])
graph2 = Graph([[3,4],[4,5],[4,6],[4,7],[3,1],[1,2],[2,3],[8,5],[8,6],[9,3],[9,4]])
graph3 = Graph([[0, 1], [1, 2], [1, 4], [4, 5], [4, 3], [3, 1], [3, 6]])
print(graph3.bfs())
graph3.set_distance_and_previous(2)
'''
for item in graph3.nodes_by_id:
	print(graph3.nodes_by_id[item].id)
	print(graph3.nodes_by_id[item].distance)
	print('')
print(graph3.nodes_by_id)
print(graph3.calc_distance(0,3))
print(graph3.calc_distance(3,5))
print(graph3.calc_distance(0,5))
print(graph3.calc_distance(4,1))
print(graph3.calc_distance(2,4))
print(graph3.calc_shortest_path(0,3))
print(graph3.calc_)
'''