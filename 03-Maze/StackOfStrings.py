class Node:

    def __init__(self):
        self.item = ""
        self.next = None
	
class StackOfStrings:

    def __init__(self):
        self.first = None

    # Add a new string to the stack
    def push(self, s):
        node = Node()
        node.item = s;

        if self.first == None:
            self.first = node
        else:
            node.next = self.first
            self.first = node

    # Remove the most recently added string
    def pop(self):
        if self.first == None:
            throw ("Stack is empty!")
        result = self.first.item
        self.first = self.first.next
        return result

    # Return a string representation of the stack	
    def toString(self):
        result = ""
        current = self.first
        while current != None:
            result += current.item
            result += " "
            current = current.next
        return result

    # Check if the stack is empty
    def isEmpty(self):
        return self.first == None
    
# main method for testing out the class
if __name__ == "__main__":
    q = StackOfStrings()

    print("stack = " + q.toString())

    q.push("this")
    print(q.toString())

    print("pop = " + q.pop())
    print(q.toString())

    q.push("a")
    q.push("b")
    q.push("c")
    print(q.toString())

    print("pop = " + q.pop())
    print(q.toString())
    print("pop = " + q.pop())
    print(q.toString())
    print("pop = " + q.pop())
    print(q.toString())		
