from ortools.sat.python import cp_model
from mars_planner import *
from routefinder import *
from mapcoloring import *

# QUESTION 2
s = RoverState()

print("DFS for Mission Complete")
result2 = depth_first_search(s, action_list, mission_complete)
print(result2, '\n')

print("DLS with limit = 2 for Mission Complete")
result3 = depth_first_search(s, action_list, mission_complete, limit = 2)
print(result3, '\n')

print("BFS for Mission Complete")
resultBFS = breadth_first_search(s, action_list, mission_complete)
print(resultBFS, '\n')

print("BFS for moveToSample")
moveToSampleBFS = breadth_first_search(s, action_list, sample_goal)
print(moveToSampleBFS, '\n')

print("BFS for removeSample")
removeSampleBFS = breadth_first_search(s, action_list, sample_remove_goal)
print(removeSampleBFS, '\n')

print("BFS for returnToCharger")
returnToChargerBFS = breadth_first_search(s, action_list, battery_goal)
print(returnToChargerBFS)

# QUESTION 3 
my_mars_graph = read_mars_graph('marsdata.txt')
    # for node, edges in my_mars_graph.g.items():
    #     print(f"Node {node}:")
    #     for edge in edges:
    #         print(f"  {edge}")

my_m = map_state(location = '8,8', mars_graph=my_mars_graph)
print("A* for Question 3: ")
my_a = a_star(my_m, sld, goal_test)

print("UCS for Question 3: ")
my_a = a_star(my_m, h1, goal_test)

# QUESTION 4
print("A1: %s" % freqs[solver.Value(A1)])
print("A2: %s" % freqs[solver.Value(A2)])
print("A3: %s" % freqs[solver.Value(A3)])
print("A4: %s" % freqs[solver.Value(A4)])
print("A5: %s" % freqs[solver.Value(A5)])
print("A6: %s" % freqs[solver.Value(A6)])
print("A7: %s" % freqs[solver.Value(A7)])
print("A8: %s" % freqs[solver.Value(A8)])
print("A9: %s" % freqs[solver.Value(A9)])