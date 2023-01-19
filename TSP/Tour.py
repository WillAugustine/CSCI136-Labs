import StdDraw
import Point

class Node:
    def __init__(self):
        self.p = None
        self.next = None

class Tour:
    def __init__(self):
        self.tour = []

    def show(self):
        for stop in self.tour:
            print(stop)

    def draw(self):
        pass

    # return int
    def size(self):
        return len(self.tour)

    # return float
    def distance(self):
        pass

    def insertInOrder(self, p):
        self.tour.append(p)

    def insertNearest(self, p):
        pass

    def insertSmallest(self, p):
        pass


