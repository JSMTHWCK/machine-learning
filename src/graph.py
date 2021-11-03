class Graph:
	def __init__(self,edges):
		self.edges = edges
		self.parents = [edge[0]  for edge in edges]
		self.children = [edge[1] for edge in edges]

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
			queue_copy = queue
			for item in queue:
				if item not in visited:
<<<<<<< HEAD
					#the problem is it makes it an unlisted index (so basically it tries to find index 9 not #9)
=======
>>>>>>> c1691784605b3535675f55d651e376004355d7ff
					visited[str(item)] = True
					order.append(item)
					for item in self.get_children(queue[0]):
						queue.append(item)			
				queue.pop(0)

					

		return order


graph = Graph([[2,8],[9,3],[1,5],[9,6],[9,6],[6,9],[4,5],[10,6],[3,10],[8,7],[8,5],[6,2],[8,10],[6,1],[6,4]])
graph2 = Graph([[1,2],[2,4],[2,3],[3,6],[3,5]])
print(graph.get_parents(6))
print(graph.bfs())

