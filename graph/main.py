"""
Graphs is a data structure that consists of a set of:
- nodes/vertices
- nodes are connected by links/edges
Types of graphs:
1. Directed graphs:
    - specific direction
2. Undirected graphs:
    - edges have no direction
    - Assumes the relationship is mutual
3. Weighted graphs:
    - Numeric values associaated with the edges
    - can be either directed or undirected.

* Differnces between graphs and tress
Trees
- Cannot have cycles
- All nodes must be connected

Graphs
- Can have cycles
- Some nodes can remain unconnected

# Real World Cases
1. User relationships in social networks
    - frienship
    - follows
    - likes
2. Locaations and distances
    - optimixe routes
3. Graph databases
"""

# Graph - implementation
class Graph:
    """A graph class used to represent a graph. contains methods to add vertices and egdes (connections between vertices)"""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self,source, target):
        self.vertices[source].append(target)

"""
1. The above implementation represents a directed graph because the edges are added in a specific direction from source to target
2. The graph is unwighted, meaning the edges do not have an associated numberic values
3. The add_edge assumes both source and target

"""
graph = Graph()
graph.add_vertex("David")
graph.add_vertex("Miriam")
graph.add_vertex("Martin")
graph.add_edge("David","Martin" )
graph.add_edge("David","Miriam" )
graph.add_edge("Miriam",  "Martin")
print(graph.vertices)

class WeightedGraph:
    def __init__(self):
        self.vertices

    def add_vertex(self, vertex):
        self.vertics[vertex] = []

    def add_edge(self, source, target, weight):
        self.vertices[source].append(target, weight)

my_graph = WeightedGraph()

# create the vertices
my_graph.add_vertex("Paris")
my_graph.add_vertex("Toulouse")
my_graph.add_vertex("Biaritz")

my_graph.add_edge("Paris", "Toulouse", 678)
my_graph.add_edge("Toulouse", "Biaritz" ,312)
my_graph.add_edge("Paris", "Biarritz", 783)
