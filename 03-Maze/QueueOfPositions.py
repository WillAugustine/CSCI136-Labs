from Position import Position
class Node:

    def __init__(self):
        self.item = ""
        self.next = None

class QueueOfStrings:

    def __init__(self):
        self.first = None
        self.last  = None

    # Add a new string to the queue
    def enqueue(self, position):
        node = Node()
        node.item = position
        node.next = None

        if self.last != None:
            self.last.next = node
        self.last = node

        if self.first == None:
            self.first = node

    # Remove the least recently added string
    def dequeue(self):
        if self.first == None:
            throw ("Queue is empty!")
        result = self.first.item
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return result.toString()

    # Return a string representation of the queue	
    def toString(self):
        result = ""
        current = self.first
        while current != None:
            result += current.item.toString()
            current = current.next
        return result
	
    def isEmpty(self):
        return self.first == None
    
# main method for testing out the class
if __name__ == "__main__":
    q = QueueOfStrings()
    a = Position(0,0)
    b = Position(2,0)
    c = Position(2,2)
    d = Position(0,2)
    print("queue = " + q.toString())
    
    q.enqueue(a)
    print(q.toString())

    print("dequeue = " + q.dequeue())
    print(q.toString())

    q.enqueue(b)
    q.enqueue(c)
    q.enqueue(d)
    print(q.toString())

    print("dequeue = " + q.dequeue())
    print(q.toString())
    print("dequeue = " + q.dequeue())
    print(q.toString())
    print("dequeue = " + q.dequeue())
    print(q.toString())
