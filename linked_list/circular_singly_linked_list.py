

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    
    # add new element at the end of the list
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
        
    # add new element at the beginning of the list
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

    # 1-based indexing
    def add_by_index(self, value, index):
        if index < 1 or index > self.length + 1:
            return False
        
        count_index = 0
        curr_node = self.head
        new_node = Node(value)

        while count_index < index:
            curr_node = curr_node.next
            count_index += 1
        
        next_node = curr_node.next
        curr_node.next = new_node
        new_node.next = next_node




if __name__ == '__main__':
    circular_linked_list = CircularSinglyLinkedList()
    


        

            
            
            
        
            
        
    
    
    
        