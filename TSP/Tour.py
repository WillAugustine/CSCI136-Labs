#
# Author: Will Augustine, CS Student at Montana Tech
# Description: Complete solution of the CSCI 136 Spring 2023
#   Traveling Sales Person (TSP) lab
#

import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import StdDraw
from Point import Point
import pygame
import math
import sys

# Class for nodes - individual components of the linked list
class Node:
    def __init__(self):
        # self.p represents that node's data
        self.p = None
        # self.next represents what that node points to (the next node)
        self.next = None

# Class for the linked list made up of nodes
class Tour:
    def __init__(self):
        # The starting tour is empty
        self.tour = None
    
    # Function to get the size of the linked list
    def size(self):
        # If the linked list is empty, return 0 as the length
        if self.tour == None:
            return 0
        # Otherwise, traverse through the linked list and return the count
        else:
            count = 0
            # Create copy of self.tour so the starting place never changes
            node = self.tour
            # While the current node is not empty
            while node != None:
                # Set the node to 
                node = node.next
                count += 1
            return count
    
    def show(self):
        node = self.tour
        while node.next != None:
            print(node.p.toString())
            node = node.next
        print(f"{node.p.toString()}\n")

    def distance(self):
        totalDistance = 0
        node = self.tour
        firstNode = node
        while node.next != None:
            totalDistance += node.p.distanceTo(node.next.p)
            node = node.next
        totalDistance += node.p.distanceTo(firstNode.p)
        return totalDistance

    def draw(self):
        node = self.tour
        firstNode = node
        while node.next != None:
            node.p.drawTo(node.next.p)
            node = node.next
        node.p.drawTo(firstNode.p)

    def insertInOrder(self, p):
        newNode = Node()
        newNode.p = p
        if self.tour == None:
            self.tour = newNode
        else:
            temp = self.tour
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def insertNearest(self, p):
        newNode = Node()
        newNode.p = p
        if self.tour == None:
            self.tour = newNode
        else:
            temp = self.tour
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

    def insertSmallest(self, p):
        newNode = Node()
        newNode.p = p
        if self.tour == None:
            self.tour = newNode
        else:
            temp = self.tour
            while temp.next != None:
                temp = temp.next
            temp.next = newNode

if __name__ == "__main__":
    tour = Tour()
    a = Point(100.0, 100.0)
    b = Point(500.0, 100.0)
    c = Point(500.0, 500.0)
    d = Point(100.0, 500.0)

    tour.insertInOrder(a)
    tour.insertInOrder(b)
    tour.insertInOrder(c)
    tour.insertInOrder(d)

    print("The current tour is:")
    tour.show()

    print(f"The size of the current tour is {tour.size()}")
    
    print(f"The distance of the current tour is {tour.distance()}")

    StdDraw.setCanvasSize(600,600)
    StdDraw.setXscale(0, 600)
    StdDraw.setYscale(0, 600)
    tour.draw()
    StdDraw.show(1000)
    StdDraw.save("test.png")