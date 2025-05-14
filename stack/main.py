"""Stacks -  Implementation using singly linked list """
"""
    LIFO
1. Can only insert at the end 
2. Can only remove from the end


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
            self.top = new_node
        else:
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

# LifoQueue in Python
"""
1. Python queue module
2. behaves like a stack
"""
import queue

my_book_stack = queue.LifoQueue(maxsize=0)
my_book_stack.put("The misunderstanding")
my_book_stack.put("Perspolis")
my_book_stack.put("1984")
popped = my_book_stack.get("")

one = my_book_stack.qsize()
print(one)
