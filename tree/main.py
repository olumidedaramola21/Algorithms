"""
    Tree - definition
- Node-based data structure
- Each node can have links to more than one node
- first node is called a root
- A node can be the parent of other nodes which are called children.
- A tree can have many levels.

Types Of Tree
1. Binary Tree
- Each node has:
    - Zero children
    - One children
    - Two children
"""

class BinaryTreeNode:
    """Binary Tree Implementation"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

node1 = BinaryTreeNode("B")
node2 = BinaryTreeNode("C")
root_node = BinaryTreeNode("A", node1, node2)

"""
Trees - real uses
1. Storing hierachical relationships
    - File system of a computer
    - structure of an HTML document
2. Chess: possible moves of the rival.
3. Searching and sorting algorithms.
"""
