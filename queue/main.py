"""Queues Implementation"""
"""
    FIFO
1. Enqueue: Can only at the end (add to the tail)
2. Dequeue: Can only remove from the head
    - Types of Queues include:
    1. Doubly ended queues
    2. Circular queues
    3. Priority queues
    - Real world use cases
    1. Printing tasks in a printer
    2. Applications where the order of request matter
        1. Tickets in a concert
        2. Taxi services
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """Insert node at the end"""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """Remove node from the beginning"""
        if self.head:
            current_node = self.head
            self.head = current_node.next
        
        if self.head == None:
            self.tail = None

"""SimpleQueue in Python"""
""""
- Module: queue offers these two:
- Queue
- SimpleQueue

    - put()
    -get(): removes and returns the removed element
    - empty()

"""
"""SimpleQueue Implementation"""
import queue

order_queue = queue.SimpleQueue()

order_queue.put("Rice")
order_queue.put("Beans")
order_queue.put("Yam and egg")

print("The size is: ", order_queue.size())

print(order_queue.get())
print(order_queue.get())
print(order_queue.get())

print("Empty queue: ", order_queue.empty())

"""Queue Implementation"""
class PrinterTasks:
    def __init__(self):
        self.queue = Queue()

    def add_document(self, document):
        self.queue.enqueue(document)

    def has_elements(self):
        return self.head != None 

    def print_document(self):
        while self.queue.has_elements():
            self.queue.dequeue()
