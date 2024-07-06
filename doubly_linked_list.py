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
        self.length = 0
        
        
        
    def append(self, value):
        new_node = Node(value)
        self.length += 1
        
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
        self.length += 1
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        temp_node.prev = self.head
    
    
    # Add element to the doubly linked list by index
    def add_by_index(self, index, value):
        if self.length < index or index  < 0:
            return
        
        if index == self.length:
            self.append(value)
            return
        if index == 0: 
            self.prepend(value)
            return
           
        new_node = Node(value)
        if index <= (self.length//2):
            counter = 0
            temp_node = self.head
            while counter < index - 1:
                temp_node = temp_node.next
                counter += 1
            new_node.next = temp_node.next
            temp_node.next.prev = new_node
            temp_node.next = new_node
            new_node.prev = temp_node
                
        else:
            counter = self.length - 1
            temp_node = self.tail
            while counter > index:
                temp_node = temp_node.prev
                counter -= 1
            
            new_node.prev = temp_node.prev
            temp_node.prev.next = new_node
            new_node.next = temp_node
            temp_node.prev = new_node
            
        self.length += 1
            
        
        
        
    
    
        
    
    
    # print element from beginning to ending
    def display_forward(self):
        if self.head == None:
            print("Empty Doubly Linked List")
        
        print("The size of the Doubly Linked List: ", self.length)
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
        
        print("The size of the Doubly Linked List: ", self.length)    
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
    doublyLinkedList.append(88)
    
    doublyLinkedList.display_forward()
    doublyLinkedList.display_backward()
    
    doublyLinkedList.add_by_index(0, 5000)
    doublyLinkedList.add_by_index(9, 5000)
    doublyLinkedList.add_by_index(7, 5000)
    
    
    doublyLinkedList.display_forward()
    doublyLinkedList.display_backward()
    
    
    
    
