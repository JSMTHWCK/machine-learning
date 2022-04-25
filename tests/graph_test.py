import sys
import math
sys.path.append('src')

from graph import *
'''<-----set not 23 ------>'''
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
if grapha.bfs() != [4,0,8,6,2,3,1,9,5,7]:
    print("bfs failed on ",grapha.edges)
if grapha.dfs() != [4,6,3,5,7,9,1,2,8,0]:
    print("dfs failed on ",grapha.edges)
if graphb.bfs() != [0,1,2,3,4,5,6,7,8]:
    print("bfs failed at ",graphb.edges)
if graphb.dfs() != [0,3,6,8,7,5,4,2,1]:
    print("dfs failed at ",graphb.edges)

'''<----set yes 23 ----->'''
print('start')
graph3 = Graph([[0, 1], [1, 2], [1, 4], [4, 5], [4, 3], [3, 1], [3, 6]])
if graph3.calc_distance(0,3) != 3:
    print('calc_distance failed')
    print('want 3')
    print('got ',graph3.calc_distance(0,3))
    assert graph3.calc_distance(0,3) == 3

if graph3.calc_distance(3,5 ) != 3:
    print('calc_distance failed')
    print('want 3')
    print('got ',graph3.calc_distance(3,5))
    assert graph3.calc_distance(3,5) == 3

if graph3.calc_distance(0,5) != 3:
    print('calc_distance failed')
    print('want 3')
    print('got ',graph3.calc_distance(0,5))
    assert graph3.calc_distance(0,5) == 3

if graph3.calc_distance(4,1) != 2:
    print('calc_distance failed')
    print('want 2')
    print('got ',graph3.calc_distance(4,1))
    assert graph3.calc_distance(4,1) == 2

if graph3.calc_distance(2,4) != False:
    print('calc_distance failed')
    print('want false')
    print('got ',graph3.calc_distance(2,4))
    assert graph3.calc_distance(2,4) == False

'''-----------------------'''
if graph3.calc_shortest_path(0,3) != [0,1,4,3]:
    print('calc_distance failed')
    print('want 3')
    print('got ',graph3.calc_shortest_path(0,3))
    assert graph3.calc_shortest_path(0,3) == [0,1,4,3]
graph3.set_distance_and_previous(3)
if graph3.calc_shortest_path(3,5) != [3,1,4,5]:
    print('calc_distance failed')
    print('want 3')
    print('got ',graph3.calc_shortest_path(3,5))
    assert graph3.calc_shortest_path(3,5) == [3,1,4,5]

if graph3.calc_shortest_path(0,5) != [0,1,4,5]:
    print('calc_distance failed')
    print('want 3')
    print('got ',graph3.calc_shortest_path(0,5))
    assert graph3.calc_shortest_path(0,5) == [0,1,4,5]

if graph3.calc_shortest_path(4,1) != [4,3,1]:
    print('calc_distance failed')
    print('want 2')
    print('got ',graph3.calc_shortest_path(4,1))
    assert graph3.calc_shortest_path(4,1) == [4,3,1]

if graph3.calc_shortest_path(2,4) != False:
    print('calc_distance failed')
    print('want false')
    print('got ',graph3.calc_shortest_path(2,4))
    assert graph3.calc_shortest_path(2,4) == False
print('end')
'''<------------------ set 25 ------------------>'''
#--------------------------------------------------
from graph_weight import *
values = {
    (0,1): 3, (1,0): 3,
    (1,7): 4, (7,1): 4,
    (7,2): 2, (2,7): 2,
    (2,5): 1, (5,2): 1,
    (5,6): 8, (6,5): 8,
    (0,3): 2, (3,0): 2,
    (3,2): 6, (2,3): 6,
    (3,4): 1, (4,3): 1,
    (4,8): 8, (8,4): 8,
    (8,0): 4, (0,8): 4
}

a = WeightedGraph(values)
print('hi')

for i in range(0,9):
    print(i)
    a.calc_shortest_path(8,i)