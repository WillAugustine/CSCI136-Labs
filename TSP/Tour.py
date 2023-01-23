#
# Author: Will Augustine, CS Student at Montana Tech
# Description: Complete solution of the CSCI 136 Spring 2023
#   Traveling Sales Person (TSP) lab
#

import os
#os.environ["SDL_VIDEODRIVER"] = "dummy"
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

# Class for the linked list made up of nodes (circular)
class Tour:
    def __init__(self):
        # The starting tour is empty 
        self.tour = None
        # Counter to 
        self.length = 0
    
    # Function to get the size of the linked list
    def size(self):
        # If the linked list is empty, return 0 as the length
        if self.tour == None:
            return 0
        # Otherwise, traverse through the linked list and return the count
        else:
            firstNode = self.tour
            count = 1
            # Create copy of self.tour so the starting place never changes
            node = self.tour
            # While the current node is not empty
            while node.next != firstNode:
                # Set the node to 
                node = node.next
                # Increment count
                count += 1
            # Return the size of the linked list
            return count
    
    # Method to show each item in the tour
    def show(self):
        firstNode = self.tour
        node = self.tour
        while node.next != firstNode:
            print(node.p.toString())
            node = node.next
        print(f"{node.p.toString()}\n")

    def distance(self):
        totalDistance = 0
        node = self.tour
        firstNode = node
        while node.next != firstNode:
            totalDistance += node.p.distanceTo(node.next.p)
            node = node.next
        totalDistance += node.p.distanceTo(firstNode.p)
        return totalDistance

    def draw(self):
        node = self.tour
        firstNode = self.tour
        while node.next != firstNode:
            node.p.drawTo(node.next.p)
            node = node.next
        node.p.drawTo(firstNode.p)

    def insertInOrder(self, p):
        newNode = Node()
        newNode.p = p
        if self.tour == None:
            newNode.next = newNode
            self.tour = newNode
        else:
            firstNode = self.tour
            temp = self.tour
            while temp.next != firstNode:
                temp = temp.next
            newNode.next = firstNode
            temp.next = newNode


    def insertNearest(self, p):
        """Insert point p using nearest neighbor heuristic."""
        node = Node()
        node.p = p
        bestNode = Node()
        if not self.tour:
            self.tour = node
            self.tour.next = self.tour
        else:
            current = self.tour            
            bestDist = float('inf')
            # Walks through list and searches for the 
            # location that is closet to the new node
            for x in range(self.length):
                distance = current.p.distanceTo(node.p)
                if distance < bestDist:
                    bestDist = distance
                    bestNode = current  
                current = current.next
            node.next = bestNode.next  # Links new node up, order is important
            bestNode.next = node

    def insertSmallest(self, p):
        """Insert point p using smallest increase heuristic."""
        node = Node()
        node.p = p
        if not self.tour:
            self.tour = node
            self.tour.next = self.tour
        else:
            current = self.tour            
            bestDist = float('inf')
            # Walks through list searching for the point that 
            # would decrease the total tour amount the greatest.
            for x in range(self.length):
                distance = self.distance() + \
                           current.p.distanceTo(node.p) + \
                           current.next.p.distanceTo(node.p) - \
                           current.next.p.distanceTo(current.p)
                if distance < bestDist:
                    bestDist = distance
                    bestNode = current  
                current = current.next
            node.next = bestNode.next
            bestNode.next = node
        self.length += 1

if __name__ == "__main__":
    # tour = Tour()
    # a = Point(100.0, 100.0)
    # b = Point(500.0, 100.0)
    # c = Point(500.0, 500.0)
    # d = Point(100.0, 500.0)

    # tour.insertInOrder(a)
    # tour.insertInOrder(b)
    # tour.insertInOrder(c)
    # tour.insertInOrder(d)

    # print("The current tour is:")
    # tour.show()

    # print(f"The size of the current tour is {tour.size()}")
    
    # print(f"The distance of the current tour is {tour.distance()}")

    # StdDraw.setCanvasSize(600,600)
    # StdDraw.setXscale(0, 600)
    # StdDraw.setYscale(0, 600)
    # tour.draw()
    # StdDraw.show(1000)
    # StdDraw.save("test.png")
    pass