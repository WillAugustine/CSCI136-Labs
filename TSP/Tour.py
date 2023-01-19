import StdDraw
from Point import Point
import pygame
import math
import sys

class Node:
    def __init__(self):
        self.p = None
        self.next = None

class Tour:
    def __init__(self):
        #self.tour = []
        self.tour = None

    def getXY(self, p):
        XY = [p.x, p.y]
        return XY

    def show(self):
        tour = self.tour
        while tour is not None:
            print(tour)
            tour = tour.next

        # for stop in self.tour:
        #     print(f"({stop.x} {stop.y})")

    def draw(self):
        size = len(self.tour)
        for i in range(0, size-1):
            x1, y1 = self.getXY(self.tour[i])[0], self.getXY(self.tour[i])[1]
            x2, y2 = self.getXY(self.tour[i+1])[0], self.getXY(self.tour[i+1])[1]

            #print(f"({x1}, {y1}) -> ({x2}, {y2})")
            StdDraw.line(x1, y1, x2, y2)

        x1, y1 = self.getXY(self.tour[size-1])[0], self.getXY(self.tour[size-1])[1]
        x2, y2 = self.getXY(self.tour[0])[0], self.getXY(self.tour[0])[1]

        #print(f"({x1}, {y1}) -> ({x2}, {y2})")
        StdDraw.line(x1, y1, x2, y2)

    # return int
    def size(self):
        count = 0
        tour = self.tour
        while tour.next != None:
            count += 1
            tour = tour.next
        #print(count)
        return count
        #return len(self.tour)

    # return float
    def distance(self):
        totalDistance = 0.0
        size = len(self.tour)
        for i in range(0, size-1):
            x1, y1 = self.getXY(self.tour[i])[0], self.getXY(self.tour[i])[1]
            x2, y2 = self.getXY(self.tour[i+1])[0], self.getXY(self.tour[i+1])[1]
            totalDistance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        x1, y1 = self.getXY(self.tour[size-1])[0], self.getXY(self.tour[size-1])[1]
        x2, y2 = self.getXY(self.tour[0])[0], self.getXY(self.tour[0])[1]
        totalDistance += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return totalDistance

    def insertInOrder(self, p):
        newNode = Node()
        newNode.p = p
        newNode.next = None
        if self.tour == None:
            self.tour = newNode
        else:
            self.tour.next = newNode
        #self.tour.append(p)

    
    def findClosest(self, p):
        x, y = self.getXY(p)[0], self.getXY(p)[1]
        smallestDistance = 0
        for point in self.tour:
            currX, currY = self.getXY(point)[0], self.getXY(point)[1]
            currDistance = self.distance(x, y, currX, currY)
            
    # add p after closest point
    def insertNearest(self, p):
        pass

    # add p where tour results in smallest tour length
    def insertSmallest(self, p):
        pass

if __name__ == "__main__":
    #filename = sys.argv[1]

    tour = Tour()

    a = Point(100.0, 100.0)
    b = Point(500.0, 100.0)
    c = Point(500.0, 500.0)
    d = Point(100.0, 500.0)

    tour.insertInOrder(a)
    tour.insertInOrder(b)
    tour.insertInOrder(c)
    tour.insertInOrder(d)

    print(f"The current tour is:\n{tour.show()}")

    print(f"The size of the current tour is {tour.size()}")
    


