class Node:
    def __init__(self, data):
        self.data = data    # data stored
        self.next = None    # pointer to the next Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        # LinkedList - methods
        """
        1. insert_at_beginning()
        2. remove_at_beginning()
        3. insert_at_end()
        4. remove_at_end()
        5. insert_at()
        6. remove_at()
        7. search()

        """
    
    def insert_at_beginning(self, data):
        """Insert at the beginning"""
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def remove_at_beginning(self):
        """Remove the first node of the linked list"""
        if self.head is None:
            # List is already empty
            print("List is empty. Nothing to remove")
            return
        self.head = self.head.next
        # if list becomes empty after removing the head.
        if self.head is None:
            self.tail = None


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
