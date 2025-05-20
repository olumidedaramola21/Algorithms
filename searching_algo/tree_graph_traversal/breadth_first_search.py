"""
Breadth First Search - binary tree
    - starts from root
    - visits every node at every level

    complexity O(n)
"""

# Breadth-First Search (BFS) - trees

import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def bfs_tree(self):
        """
        - visited_nodes
        - bfs_qu
        """
        if self.root:
            visited_nodes = []
            bfs_queue = queue.SimpleQueue()
            bfs_queue.put(self.root)

        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_nodes.append(current_node)
            if current_node.left:
                bfs_queue.put(current_node.left)
            if current_node.right:
                bfs_queue.put(current_node.right)

        return visited_nodes


"""
Breadth First Search - graphs
    - Graphs can have cycles
        - need to check is the vertices are already visited

    comp  lexity O(V + E)
"""

def bfs_graph(graph, initial_vertex):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)

    while not bfs_queue.empty():
        current_vertex = bfs_queue.get() 
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)

    return visited_vertices

"""
BFS VS DFS

BFS
    - Target close to the starting vertex
    - Applications:
        - Web crawling
        - Finding shortest path in unweighted graphs
        - Finding connected locations using GPS
        - Used as part of other more complex algorithms

DFS
    - Target far away from the starting vertex
    - Applications:
        - Solving puzzles with only one solution
        - Detecting cycles in graphs
        - Finding shortest path in a weighted graph
        - Used as part of other more complex algorithms
"""


# Findind a graph vertex using graph
import queue

def bfs_find(graph, initial_vertex, search_value):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    visited_vertices.append(initial_vertex)
    bfs_queue.put(initial_vertex)

    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        # check if current vertex is search value
        if current_vertex == search_value:
            return True
        for adjacent_vertex in graph[current_vertex]:
            # check if adjacent vertex has been visited
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
          
    # return false if search value is not found
    return False
