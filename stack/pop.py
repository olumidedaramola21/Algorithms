class Node:
    def __init__(self, data):
        self.top = data
        self.next = None
    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data
        

