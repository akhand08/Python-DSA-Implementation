

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.length += 1
            return
        
        counter = 0
        temp_node = self.head
        while counter < self.length:
            temp_node = temp_node.next
            counter += 1
        
        temp_node.next = new_node
        new_node.next = self.head
        self.length += 1
        
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        
        counter = 0
        temp_node = self.head
        while counter < self.length:
            temp_node = temp_node.next
            counter += 1
            
        temp_node.next = new_node
        new_node.next = self.head
        self.head = new_node
            
            
        
            
        
    
    
    
        