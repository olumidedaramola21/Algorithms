"""
Definition
- Left subtree of a node:
    - contains values less than the node itself
- Right substree of node:
    - contains values greater than the node itself
- Left and Right substrees must be binary search trees
"""

# Implementation:
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, search_value):
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False

    def insert(self, data):
        new_node = TreeNode(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if current_node.left_child == None:
                        current_node.left_child = new_node
                        return
                    else:
                        current_node = current_node.left_child
                elif current_node > data:
                    if current_node.right_child == None:
                        current_node.right_child = new_node
                        return
                    else:
                        current_node = current_node.right_child 

    # Finding the minimum node of a BST
    def find_min_node(self):
        current_node = self.root
        while current_node.left_child:
            current_node = current_node.left_child
        return current_node.data
    
    # Finding the max node of a BST
    def find_max_node(self):
        current_node = self.root
        while current_node.right_child:
            current_node = current_node.right_child
        return current_node.data


                        
        # delete operation
        """
        1. No children
            - delete it#
        2. 1 child
            - delete node and connect the child with parent node
        2. 2 children
            - replace with its successor (successor is node with smallest value greater than the value of the node.)
            - To find the successor:
                - Visit the right node
                - keep visiting the left node until then
            - if successor has  a right child:
                - child becomes the left child of the successor's parent.

        """

"""
Uses
1. Order lists efficiently
2. Much faster at searching than arrays and linked lists.
3. Much faster at inserting and deleting than arrays
4. Used to implement more advanced data structures
    - dynamic sets
    - lookup tables
    - prioty queues
"""

"""

"""


