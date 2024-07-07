
# create node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.count_element = 0
        
    
    # add new element to the end
    def append(self, value):
        self.count_element += 1
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        curr_node = self.head
        
        while curr_node.next != None:
            curr_node = curr_node.next
        
        curr_node.next = new_node
        
    
    # add new element to the beginning
    def prepend(self, value):
        self.count_element += 1
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        
    # add new element on your given index
    def add_by_index(self, value, index):
        if index < 0 or index > self.count_element:
            return
        
        self.count_element += 1
        new_node = Node(value)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        count_index = 0
        curr_node = self.head
        while count_index+1 != index:
            curr_node = curr_node.next
            count_index += 1
        
        new_node.next = curr_node.next
        curr_node.next = new_node
            
            

    #  delete any element matched by your value (first occurance)
    def delete_by_value(self, value):
        deleted_node = self.head
        prev_node = self.head
        
        
        while deleted_node.value != value:
            prev_node = deleted_node
            deleted_node = deleted_node.next
            
            if deleted_node == None:
                return  False
    

        
        self.count_element -= 1
        prev_node.next = deleted_node.next
            
    
    
    
    
    
    
    # delete element based on given index
    def delete_by_index(self, index):  # 0-th index linked list
        if self.count_element == 0 or index  >= self.count_element:
            return
        
        self.count_element -= 1
        if index == 0:
            self.head = self.head.next
            return
        
        count_index = 0
        deleted_node = self.head
        prev_node = self.head
        
        while count_index != index:
            prev_node = deleted_node
            deleted_node = deleted_node.next 
            count_index += 1
        
        prev_node.next = deleted_node.next
            
        
        
        
        
    # find the length of the linked list
    def length(self):
        return self.count_element
    
    
    # search() will return index based upon given value
    def search(self, value):
        if self.head == None:
            return -1
        
        
        new_node = self.head
        counter = 0
        
        while new_node != None:
            if new_node.value == value:
                return counter
            else:
                counter += 1
                new_node = new_node.next
        
        
            
            
        
    # print the Linked List
    def print(self):
        printList = self.head
        
        
        
        
        print("The Singly Linked List: " , end="")
        while printList is not None:
            print(printList.value, end="")
            if printList.next != None:
                print(" -> ", end="")
            printList = printList.next
        
        print()
        



if __name__ == '__main__':
    linked_list = LinkedList()
    
    
    linked_list.prepend(10)
    
    linked_list.prepend(20)
    linked_list.add_by_index(500,1)
    linked_list.add_by_index(333,2)
    linked_list.prepend(21)
    
    
    linked_list.print()
    # The Singly Linked List: 21 -> 20 -> 500 -> 333 -> 10
    
    print(linked_list.search(10))
    # Output -> 4
    
    linked_list.add_by_index(877,1)
    linked_list.add_by_index(3,2)
    linked_list.prepend(21)
    linked_list.delete_by_index(1)
    linked_list.print()
    # The Singly Linked List: 21 -> 877 -> 3 -> 20 -> 500 -> 333 -> 10
    
    
   
