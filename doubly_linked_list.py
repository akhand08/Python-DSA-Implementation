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
        
        temp_node = self.tail
        temp_node.next = new_node
        self.tail = new_node
        
    
    
    # print element from beginning to ending
    def display_forward(self):
        if self.head == None:
            print("Empty Linked List")
        
        curr_node = self.head
        print("Doubly Linked List from Beginning: ", end="")
        while curr_node != None:
            print(curr_node.value, end="")
            curr_node = curr_node.next
            if curr_node != None:
                print(" -> ", end="")


 
doublyLinkedList = DoublyLinkedList()
doublyLinkedList.append(10)
doublyLinkedList.append(20)
doublyLinkedList.display_forward()
