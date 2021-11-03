import sys
import math
sys.path.append('src')

from graph import *

graph = Graph([[2,8],[9,3],[1,5],[9,6],[9,6],[6,9],[4,5],[10,6],[3,10],[8,7],[8,5],[6,2],[8,10],[6,1],[6,4]])
graph2 = Graph([[1,2],[2,4],[2,3],[3,6],[3,5]])
if graph.get_parents(6) != [9,9,10]:
    print("get_parents failed at ",graph.edges)
if graph.get_children(6) != [9,2,1,4]:
    print("get_children failed at ", graph.edges)
if graph2.get_parents(3) != [2]:
    print("get_parents failed at ",graph.edges)
if graph2.get_children(3) != [6,5]:
    print("get_children failed ",graph.edges)