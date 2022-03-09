import sys
import math
sys.path.append('src')

from graph import *

graph = Graph([[2,8],[9,3],[1,5],[9,6],[9,6],[6,9],[4,5],[10,6],[3,10],[8,7],[8,5],[6,2],[8,10],[6,1],[6,4]])
graph2 = Graph([[1,2],[2,4],[2,3],[3,6],[3,5]])

grapha = Graph([[4, 0], [4, 8], [4, 6], [0, 8], [0, 2], [0, 3], [2, 3], [3, 2], [6, 3], [3, 1], [3, 9], [3, 5], [5, 7]])
graphb = Graph([[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 4], [3, 5], [3, 6], [6, 7], [6, 8]])

if graph.get_parents(6) != [9,9,10]:
    print("get_parents failed at ",graph.edges)
if graph.get_children(6) != [9,2,1,4]:
    print("get_children failed at ", graph.edges)
if graph2.get_parents(3) != [2]:
    print("get_parents failed at ",graph.edges)
if graph2.get_children(3) != [6,5]:
    print("get_children failed ",graph.edges)
print('a is ',grapha.get_children(8))
if grapha.bfs() != [4,0,8,6,2,3,1,9,5,7]:
    print("bfs failed on ",grapha.edges)
if grapha.dfs() != [4,6,3,5,7,9,1,2,8,0]:
    print("dfs failed on ",grapha.edges)
if graphb.bfs() != [0,1,2,3,4,5,6,7,8]:
    print("bfs failed at ",graphb.edges)
if graphb.dfs() != [0,3,6,8,7,5,4,2,1]:
    print("dfs failed at ",graphb.edges)

print("hi")