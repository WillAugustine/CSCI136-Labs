from Position import Position
class Node:

    def __init__(self):
        self.item = None
        self.next = None

class QueueOfPositions:

    def __init__(self):
        self.first = None # Create empty queue
        self.last  = None # Create empty variable to represent last item in queue

    # Add a new string to the queue
    def enqueue(self, position):
        node = Node() # Create blank node that will be enqueued
        node.item = position # Add data to the node
        node.next = None # Since node will be the last item in the queue, the next value is None

        if self.last != None: # If the last value in the queue is set
            self.last.next = node # Set the last item in the queue to point to the new node
        self.last = node # Update the last variable to equal our new node

        if self.first == None: # If the queue is empty
            self.first = node # Set the first item in the queue equal to our new node

    # Remove the least recently added string
    def dequeue(self):
        if self.first == None: # If the queue is empty
            print("Queue is empty!") # Print the queue is empty
        result = self.first.item # Since we are removing the first item in the queue, set result equal to the first node
        self.first = self.first.next # Update the first node in the queue
        if self.first == None: # If the queue is now empty
            self.last = None # The last item is also empty
        return result # Return the position node dequeued

    # Return a string representation of the queue	
    def toString(self):
        result = "" # Start with a blank string to store result
        current = self.first # Set current node in traversal to first node in queue
        while current != None: # While the current node in queue is not none
            result += current.item.toString() # Add string representation of current node to result string
            current = current.next # Continue traversal through queue
        return result # Return string representation of whole queue
	
    def isEmpty(self):
        return self.first == None# Return is the first item in the queue is none (if the queue is empty)
    
# main method for testing out the class
if __name__ == "__main__":
    q = QueueOfPositions()
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
