'''Trashcan for graph.py'''
import queue
class Node:
	def __init__(self,id):
		self.id = id
		self.get_distance = 0
	def adddistance(self):
		self.get_distance += 1
	
class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.parents = [edge[0]  for edge in edges]
		self.children = [edge[1] for edge in edges]

	def nodesbyid(self):
		nodesid = {}
		for item in self.edges:
			for point in item:
				nodesid[point] = Node(point)
		self.nodesid = nodesid
					

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
				for item in self.get_children(queue[0]):
					queue.append(item)
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

	def calc_distance(self,start,end):
		self.nodesbyid()
		queue = [self.parents[0]]
		visited = {}
		order = []
		if len(visited) == len(self.nodes):
			return False
		if order[-1] == end:
			return order
		if len(queue) == 0:
			pass


graph = Graph([[2,8],[9,3],[1,5],[9,6],[9,6],[6,9],[4,5],[10,6],[3,10],[8,7],[8,5],[6,2],[8,10],[6,1],[6,4]])
graph2 = Graph([[3,4],[4,5],[4,6],[4,7],[3,1],[1,2],[2,3],[8,5],[8,6],[9,3],[9,4]])

print(graph2.dfs())
