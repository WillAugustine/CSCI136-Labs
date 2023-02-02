#   
#   Author: Will Augustine
#   Description: A class to solve a maze with a stack and then a queue
#  
#   Example of calling Solve.py:
#       "python Solve.py 5" to solve a 5x5 maze
#       "python Solve.py 8" to solve a 8x8 maze
#

# Imports
import sys
# From QueueOfPositions file, import QueueOfPositions class re-named as Queue
from QueueOfPositions import QueueOfPositions as Queue
# From StackOfPositions file, import StackOfPositions class re-named as Stack
from StackOfPositions import StackOfPositions as Stack
# From Maze file, import Maze class
from Maze import Maze
import StdDraw
# From Position file, import Position
from Position import Position

#
# The Solve class
#
class Solve:
    #
    # Constructor for the Solve class
    # 
    # @param size - the size of the maze you want to draw and solve
    #
    def __init__(self, size):
        self.stack = Stack() # Create object of Stack class
        self.queue = Queue() # Create object of Queue class
        self.maze = Maze(size) # Create object of Maze class
        self.start = None # variable for start position
        self.end = None # variable for end position
        self.solveStack = True # Boolean variable for if solving with stack or not
        self.positionsVisited = 1 # variable for number of positions visited (default = 1 because of start)

    #
    # Method to get the next available position based on current position
    # 
    # @param currPosition - object of Position class marking current position
    # 
    # @output None - there is no where to move from currPosition
    # @output nextPoint - object of Position class where the current position will move to
    #
    def getNextPosition(self, currPosition):
        if self.maze.openNorth(currPosition): # If there is no wall to the north
            nextPoint = Position(currPosition.getX(), currPosition.getY() + 1) # Set nextPoint equal to one up from currPosition
            if self.maze.isVisited(nextPoint) == False: # If nextPoint has not been visited
                return nextPoint

        if self.maze.openEast(currPosition): # If there is no wall to the east
            nextPoint = Position(currPosition.getX() + 1, currPosition.getY()) # Set nextPoint equal to one right from currPosition
            if self.maze.isVisited(nextPoint) == False: # If nextPoint has not been visited
                return nextPoint

        if self.maze.openSouth(currPosition): # If there is no wall to the south
            nextPoint = Position(currPosition.getX(), currPosition.getY() - 1) # Set nextPoint equal to one down from currPosition
            if self.maze.isVisited(nextPoint) == False: # If nextPoint has not been visited
                return nextPoint

        if self.maze.openWest(currPosition): # If there is no wall to the west
            nextPoint = Position(currPosition.getX() - 1, currPosition.getY()) # Set nextPoint equal to one left from currPosition
            if self.maze.isVisited(nextPoint) == False: # If nextPoint has not been visited
                return nextPoint
        return None # If currPosition cannot move anywhere, return None

    #
    # Method to setup the maze
    #
    def setupMaze(self):
        self.start = self.maze.getStart() # Set start value
        self.end = self.maze.getFinish() # Set end value
        self.maze.draw() # Draw the maze

    #
    # Method to reset the maze after one solution is complete
    # 
    def resetMaze(self):
        StdDraw.clear() # Wipes canvas clean
        self.maze.clear() # Clears all variables assoicated with self.maze (visited points, etc.)
        self.positionsVisited = 1 # Set the positions visited to 1 (the start)
        self.setupMaze() # Call setupMaze method to draw maze

    #
    # Method to move the marker from one spot to another
    # 
    # @param current - object of Position class marking current position
    # @param next - object of Position class marking where to go next
    # 
    # @output next - object of Position class markign where the player moved to
    #
    def movePlayer(self, current, next):
        if self.solveStack: # If solving with a stack, set colors equal to stack colors
            currentColor = StdDraw.BOOK_LIGHT_BLUE
            nextColor = StdDraw.RED
        else: # Else, set colors equal to queue colors
            currentColor = StdDraw.LIGHT_GRAY
            nextColor = StdDraw.DARK_RED
        current.draw(currentColor) # Draw previous position marker in correct color
        next.draw(nextColor) # Draw now current position marker in correct color
        StdDraw.show(750) # Show the updated maze for 750 milliseconds
        return next

    #
    # Method to solve the maze problem with both a stack and a queue
    #
    def solve(self):
        for _ in range(2): # loop through solution twice, once for stack, once for queue
            if self.solveStack: # If solving with a stack
                remove = self.stack.pop # Set remove method equal to stack's pop method
                add = self.stack.push # Set add method equal to stack's push method
            else: # Else (if solving with queue)
                remove = self.queue.dequeue # Set remove method equal to queue's dequeue method
                add = self.queue.enqueue # Set add method equal to queue's enqueue method
            currentPoint = self.start # Set current position equal to the start
            add(currentPoint) # Add the current position to the stack or queue
            self.maze.setVisited(currentPoint) # Set the current position as visited
            while not currentPoint.equals(self.end): # While the current point does not equal the finish
                nextPoint = self.getNextPosition(currentPoint) # Set the next point equal to what is returned in getNextPosition method
                if nextPoint == None: # if getNextPosition returned None
                    nextPoint = remove() # Set next position equal to first item in stack or queue
                    currentPoint = self.movePlayer(currentPoint, nextPoint) # Move back from current position to item removed from stack or queue
                else: # If getNextPosition returned a value (player was able to move)
                    add(nextPoint) # Add next position to the stack or queue
                    currentPoint = self.movePlayer(currentPoint, nextPoint) # Move the player from current point to next point and update current point to equal next point
                    self.maze.setVisited(currentPoint) # Set the newly updated current position as visited
                    self.positionsVisited += 1 # Increase the number of positions visited
            if self.solveStack: # If solving with a stack
                print(f"Solved using a stack! Visited {self.positionsVisited} spaces.") # Print message with number of positions visited
                self.resetMaze() # Reset the maze (since solving with stack is first)
            else: # Else (if solving with queue)
                print(f"Solved using a queue! Visited {self.positionsVisited} spaces.") # Print message with number of positions visited
            self.solveStack = False # Change boolean value so it solves using a queue now
    
#
# Main method (if Solve.py is called from command line)
#
if __name__ == "__main__":
    size = int(sys.argv[1]) # Get the size from command line argument
    solver = Solve(size) # Create object of Solve class, passing in desired maze size
    solver.setupMaze() # Call setupMaze method of Solve class
    solver.solve() # Call solve method of Solve class
