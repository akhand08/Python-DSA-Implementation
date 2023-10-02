# implementation of  doubly linked list 
# Using python 
# it is 0-indexed doubly linked list



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.count_element = 0
    
    
    
    # add element to the end
    def append(self, value):
        newNode = Node(value)
        self.count_element += 1
        
        if self.tail == None:
            self.head = newNode  
            self.tail = newNode
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        
        
        
        
    
    # add element to the beginning
    def prepend(self, value):
        newNode = Node(value)
        self.count_element += 1
        
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        
        
        
        
        
        
        
    # add new element on your given index
    def add_by_index(self, index, value):
        if index < 0 or index > self.count_element:
            return
        
        
        if index == 0:
            self.prepend(value)
            return
        
        if self.count_element != 0 and index == self.count_element:
            self.append(value)
            return
        
        newNode = Node(value)
        
        
        if index <= self.count_element/2:
            count_index = 0
            temp_node = self.head
            
            while count_index != index:
                temp_node = temp_node.next
                count_index += 1
            
            newNode.next = temp_node
            newNode.prev = temp_node.prev
            temp_node.prev = newNode
            
        else:
            count_index = self.count_element - 1
            temp_node = self.tail
            
            while count_index != index:
                temp_node = temp_node.prev
                count_index -= 1
            
            newNode.prev = temp_node.prev
            newNode.next = temp_node
            temp_node.prev = newNode
            
    
    
    
    # print the element form beginning to end
    def display_forward(self):
        print_node = self.head
        
        print("The Double Linked List from Beginning to End: ")
        while print_node != None:
            print(print_node.value)
            print_node = print_node.next
            
            
    # print the element from End to Beginning
    def display_backward(self):
        print_node = self.tail
        
        print("The Doubly Linked List from End to Beginning: ")
        while print_node != None:
            print(print_node.value)
            print_node = print_node.prev
            
        
        
        
                
        
            
    
        
        

        
        
        
        
        
        
        
        
        
        
                
            
            
            
            
        
        
        
        




if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.add_by_index(0,33)
    doubly_linked_list.add_by_index(1,39)
    
    doubly_linked_list.display_forward();
    doubly_linked_list.display_backward()
    
        
   