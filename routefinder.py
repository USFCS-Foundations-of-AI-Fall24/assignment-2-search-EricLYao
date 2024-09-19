from queue import PriorityQueue
from Graph import *
from math import *

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = set()
    search_queue.put(start_state)
    num_states = 0

    if use_closed_list : 
        closed_list.add(start_state)

    while not search_queue.empty():
        current_state = search_queue.get()
        num_states += 1
        if goal_test(current_state):
            print(num_states)
            return current_state
        edges = current_state.mars_graph.get_edges(current_state.location)
        for edge in edges: 
            curr_g = current_state.g + 1
            new_state = map_state(location = edge.dest, mars_graph=current_state.mars_graph, prev_state = current_state, g = curr_g)
            new_state.h = heuristic_fn(new_state)
            if new_state in closed_list and use_closed_list:
                continue
            else:
                closed_list.add(new_state)  # not in the closed list or use_closed_list is False
                search_queue.put(new_state)


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    x1, y1 = state.location.split(',')
    return sqrt((int(x1) - 1)**2 + (int(y1) - 1)**2)

def goal_test(state) :
    return state.location == "1,1"
    

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()

    with open(filename, 'r') as file:
        for line in file:
            # Splitting node and its neighbors
            node, neighbors = line.split(':')
            node = node.strip()
            neighbor_nodes = neighbors.strip().split()

            # Add the node to the graph
            graph.add_node(node)

            # Add edges for each neighbor
            for neighbor in neighbor_nodes:
                graph.add_edge(Edge(node, neighbor))

    return graph

if __name__=="__main__" :
    my_mars_graph = read_mars_graph('marsdata.txt')
    # for node, edges in my_mars_graph.g.items():
    #     print(f"Node {node}:")
    #     for edge in edges:
    #         print(f"  {edge}")

    my_m = map_state(location = '8,8', mars_graph=my_mars_graph)
    my_a = a_star(my_m, sld, goal_test)