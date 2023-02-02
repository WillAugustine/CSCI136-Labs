import sys
from QueueOfPositions import QueueOfPositions as Queue
from StackOfPositions import StackOfPositions as Stack
from Maze import Maze
import StdDraw
from Position import Position

class Solve:
    def __init__(self, size):
        self.stack = Stack()
        self.queue = Queue()
        self.maze = Maze(size)
        self.start = None
        self.end = None
        self.solveStack = True
        self.size = 0

    def getNextPosition(self, currPosition):
        if self.maze.openNorth(currPosition):
            nextPoint = Position(currPosition.getX(), currPosition.getY() + 1)
            if self.maze.isVisited(nextPoint) == False:
                return nextPoint

        if self.maze.openEast(currPosition):
            nextPoint = Position(currPosition.getX() + 1, currPosition.getY())
            if self.maze.isVisited(nextPoint) == False:
                return nextPoint

        if self.maze.openSouth(currPosition):
            nextPoint = Position(currPosition.getX(), currPosition.getY() - 1)
            if self.maze.isVisited(nextPoint) == False:
                return nextPoint

        if self.maze.openWest(currPosition):
            nextPoint = Position(currPosition.getX() - 1, currPosition.getY())
            if self.maze.isVisited(nextPoint) == False:
                return nextPoint
        return None

    def setupMaze(self):
        self.start = self.maze.getStart()
        self.end = self.maze.getFinish()
        self.maze.draw()

    def resetMaze(self):
        StdDraw.clear()
        self.maze.clear()
        self.size = 1
        self.setupMaze()

    def movePlayer(self, current, next):
        if self.solveStack:
            currentColor = StdDraw.BOOK_LIGHT_BLUE
            nextColor = StdDraw.RED
        else:
            currentColor = StdDraw.LIGHT_GRAY
            nextColor = StdDraw.DARK_RED
        current.draw(currentColor)
        next.draw(nextColor)
        StdDraw.show(750)
        return next

    def solve(self):
        for _ in range(2):
            if self.solveStack:
                remove = self.stack.pop
                add = self.stack.push
            else:
                remove = self.queue.dequeue
                add = self.queue.enqueue
            currentPoint = self.start
            add(currentPoint)
            self.maze.setVisited(currentPoint)
            while not currentPoint.equals(self.end):
                nextPoint = self.getNextPosition(currentPoint)
                if nextPoint == None:
                    nextPoint = remove()
                    currentPoint = self.movePlayer(currentPoint, nextPoint)
                else:
                    add(nextPoint)
                    currentPoint = self.movePlayer(currentPoint, nextPoint)
                    self.maze.setVisited(currentPoint)
                    self.size += 1
            if self.solveStack:
                print(f"Solved using a stack! Visited {self.size} spaces.")
                self.resetMaze()
            else:
                print(f"Solved using a queue! Visited {self.size} spaces.")
            self.solveStack = False
    

if __name__ == "__main__":
    size = int(sys.argv[1])
    solver = Solve(size)
    solver.setupMaze()
    solver.solve()
