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
        self.MAX_POSITION = size

    def getNextPosition(self, currPosition):
        nextPoint = currPosition
        if self.maze.openNorth(currPosition):
            if nextPoint.y + 1 <= self.MAX_POSITION:
                nextPoint.y += 1
            if not self.maze.isVisited(nextPoint):
                return nextPoint

        elif self.maze.openEast(currPosition):
            if nextPoint.x + 1 <= self.MAX_POSITION:
                nextPoint.x += 1
            if not self.maze.isVisited(nextPoint):
                return nextPoint

        elif self.maze.openSouth(currPosition):
            if nextPoint.y - 1 >= 0:
                nextPoint.y -= 1
            if not self.maze.isVisited(nextPoint):
                return nextPoint

        elif self.maze.openWest(currPosition):
            if nextPoint.x - 1 >= 0:
                nextPoint.x -= 1
            if not self.maze.isVisited(nextPoint):
                return nextPoint
        
        return None

    def solveWithQueue(self):
        startingPoint = self.maze.getStart()
        endingPoint = self.maze.getFinish()
        self.queue.enqueue(startingPoint)
        self.maze.setVisited(startingPoint)
        print(self.queue.toString())
        self.maze.draw()
        currentPoint = startingPoint
        while not currentPoint.equals(endingPoint):
            nextPoint = self.getNextPosition(currentPoint)
            
            if nextPoint == None:
                self.queue.dequeue()
                # self.maze.clear()
                print("DEQUEING")
            else:
                self.queue.enqueue(nextPoint)
                self.maze.setVisited(nextPoint)
                print(f"({currentPoint.toString()}) -> ({nextPoint.toString()})")
                StdDraw.show(1000)
                currentPoint = nextPoint
    

if __name__ == "__main__":
    size = int(sys.argv[1])
    solver = Solve(size)
    solver.solveWithQueue()
