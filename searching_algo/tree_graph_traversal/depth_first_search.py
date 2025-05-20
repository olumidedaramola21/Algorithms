"""
Tree/graph traversal
- Process of visiting all nodes
    -Depth first search (DFS)
    -Breadth first search (BFS)

    -Depth first search (DFS) - trees
        1. In-order
        2. Pre-order
        3. Post-order

        1. In-order traversal
            -Order: Left -> Current -> Right
            -Complexity: 0(n)

        2. Pre-order traversal
            -Order: Current -> Left -> Right
            -Complexity: 0(n)

        3. Post-order traversal
            -Order:  Left -> Right -> Current 
            -Complexity: 0(n)

    - Whent to use in-order, pre-order, and post-order
        1. In-order:
            - used BST to obtain the node's values ascending order
        2. Pre-order:
            - create copies of a tree.
            - get prefix expressions
        3. Post order:
            - delete binary trees
            - get postfix expressions


"""

    # 1. In-order traversal implementation
def in_order(self, current_node):
    if current_node:
        self.in_order(current_node.left_child)
        print(current_node.data)
        self.in_order(current_node.right_child)

    # 2. Pre-order traversal implementation
def pre_order(self, current_node):
    if current_node:
        print(current_node.data)
        self.pre_order(current_node.left_child)
        self.in_order(current_node.right_child)

    # 2. Post-order traversal implementation
def pre_order(self, current_node):
    if current_node:
        self.pre_order(current_node.left_child)
        self.in_order(current_node.right_child)
        print(current_node.data)
     

"""
Depth first search - graphs
    - Graphs can have cycles
        - need to keep track of visited vertices
    - The algorithm steps:
        - start at any vertex
        - tracks current vertex to visited vertices list
    - For each current node's adjcant vertex
        - if it has been visited -> IGNORE IT
        - if it hasn't been visited -> recursively perform DFS

Complexity:
O(V + E)
v -> number of vertices
E -> number of edges
"""

# Depth first search - implementation
def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)
