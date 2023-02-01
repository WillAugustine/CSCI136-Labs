from Position import Position

class Node:
    def __init__(self):
        self.item = None
        self.next = None
	
class StackOfPositions:
    def __init__(self):
        self.first = None # Create an empty stack

    # Add a new string to the stack
    def push(self, position):
        node = Node() # Create blank node that will be pushed
        node.item = position # Add data to the node

        if self.first == None: # If the stack is empty
            self.first = node  # Set the first item in the stack equal to the new node
        else: # If the stack is not empty
            node.next = self.first # Add the new node to the front of the stack
            self.first = node # Update what the first node in the stack is

    # Remove the most recently added string
    def pop(self):
        if self.first == None: # If the stack is empty
            print("Stack is empty!") # print that the stack is empty
        result = self.first.item # Item popped is the first item on the stack
        self.first = self.first.next # Update what the first node in the stack is
        return result.toString() # Return a string representation of position popped

    # Return a string representation of the stack	
    def toString(self):
        result = "" # Start with a blank string to store result
        current = self.first # Set current node in traversal to first node in stack
        while current != None: # While the current node in stack is not none
            result += current.item.toString() # Add string representation of current node to result string
            current = current.next # Continue traversal through stack
        return result # Return string representation of whole stack

    # Check if the stack is empty
    def isEmpty(self):
        return self.first == None # Return is the first item in the stack is none (if the stack is empty)
    
# main method for testing out the class
if __name__ == "__main__":
    q = StackOfPositions()
    a = Position(0,0)
    b = Position(2,0)
    c = Position(2,2)
    d = Position(0,2)
    print("stack = " + q.toString())

    q.push(a)
    print(q.toString())

    print("pop = " + q.pop())
    print(q.toString())

    q.push(b)
    q.push(c)
    q.push(d)
    print(q.toString())

    print("pop = " + q.pop())
    print(q.toString())
    print("pop = " + q.pop())
    print(q.toString())
    print("pop = " + q.pop())
    print(q.toString())		
