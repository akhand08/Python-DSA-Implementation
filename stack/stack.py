
#  Stack Data Structure Implementation using Python OOP

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0


    # Add item on the top of the stack
    def push(self, value):
        new_node = Node(value)
        self.length += 1

        if self.top == None:
            self.top = new_node
            return
        
        new_node.next = self.top
        self.top = new_node


    # Get and Remove the item from the top 
    def pop(self):
        if self.top == None:
            return None
        
        popped_value = self.top.value
        self.top = self.top.next 
        self.length -= 1
        return popped_value


if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())