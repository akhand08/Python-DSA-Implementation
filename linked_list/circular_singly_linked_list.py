

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
            new_node.next = self.head
            self.length += 1
            return
        

        counter = 1
        curr_node = self.head
        while counter < self.length:
            curr_node = curr_node.next
            counter += 1
        

        curr_node.next = new_node
        new_node.next = self.head
        self.length += 1




        
    # add new element at the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            self.length += 1
            return
        
        counter = 1
        curr_node = self.head
        while counter < self.length:
            curr_node = curr_node.next
            counter += 1
            
        curr_node.next = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1




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

    def display_circular_linked_list(self):
        if self.head == None:
            print("Empty Circular Linked List")
            return
        

        curr_node = self.head
        print("Circular Linked List --->  ", end = "")
        while True:
            print(curr_node.value, " --> ", end=" ")
            curr_node = curr_node.next

            if curr_node == self.head:
                break
        





if __name__ == '__main__':
    circular_linked_list = CircularSinglyLinkedList()

    circular_linked_list.append(10)
    circular_linked_list.append(30)
    circular_linked_list.append(40)
    circular_linked_list.append(50)
    circular_linked_list.prepend(100)
    circular_linked_list.prepend(200)

    circular_linked_list.display_circular_linked_list()
    


        

            
            
            
        
            
        
    
    
    
        