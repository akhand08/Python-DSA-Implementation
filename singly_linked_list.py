
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
        
        temp_node = self.head
        
        while temp_node.next is not None:
            temp_node = temp_node.next
        
        temp_node.next = new_node
        
    
    # add new element to the beginning
    def prepend(self, value):
        self.count_element += 1
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        
    # add new element on your choosen index
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
        
        count_indx = 0
        deleted_node = self.head
        prev_node = self.head
        
        while count_indx != index:
            prev_node = deleted_node
            deleted_node = deleted_node.next 
            count_indx += 1
        
        prev_node.next = deleted_node.next
            
        
        
        
        
    # find the length of the linked list
    def length(self):
        return self.count_element
    
    
    # search() will return index based upon given value
    def search(self, value):
        search_result = 0
        curr_node = self.head
        
        while curr_node != value:
            curr_node = curr_node.next
            search_result += 1
        
        if curr_node == None:
            return -1
        else:
            return search_result
            
            
        
    
    def print(self):
        printList = self.head
        
        print("The Singly Linked List: ")
        while printList is not None:
            print(printList.value)
            if printList.next != None:
                print(",")
            printList = printList.next
        



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.prepend(9890)
    linked_list.append(99)
    linked_list.append(18)
    linked_list.append(80)
    linked_list.prepend(300)
    # linked_list.add_by_index(500,1)
    
    linked_list.print()
    print("The size is: ", linked_list.length())
    linked_list.delete_by_value(18)
    print("The size is: ", linked_list.length())
    linked_list.print()
    
    
   
