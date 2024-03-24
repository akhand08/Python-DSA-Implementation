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
        self.tail = None
        
        
        
    def append(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
     
            
        temp_node = self.tail
        self.tail = new_node
        temp_node.next = self.tail
        self.tail.prev = temp_node
        
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        temp_node.prev = self.head
        
    
    
    # print element from beginning to ending
    def display_forward(self):
        if self.head == None:
            print("Empty Doubly Linked List")
        
        curr_node = self.head
        print("Doubly Linked List from Beginning: ", end="")
        while curr_node != None:
            print(curr_node.value, end="")
            curr_node = curr_node.next
            if curr_node != None:
                print(" -> ", end="")
        print()
                
    
    # print element(s) from the ending
    def display_backward(self):
        if self.tail == None:
            print("Empty Double Linked List"); 
            
        curr_node = self.tail 
        print("Doubly Linked List from Ending: ", end="")
        while curr_node != None:
            print(curr_node.value, end="")
            curr_node = curr_node.prev
            
            if curr_node != None:
                print(" -> ", end="")
        print()
        


if __name__ == "__main__":
    doublyLinkedList = DoublyLinkedList()
    
    doublyLinkedList.append(10)
    doublyLinkedList.append(20)
    doublyLinkedList.append(999)
    doublyLinkedList.append(721)
    
    
    doublyLinkedList.prepend(45)
    doublyLinkedList.prepend(808)
    doublyLinkedList.prepend(100)
    
    doublyLinkedList.display_forward()
    doublyLinkedList.display_backward()
    
    
