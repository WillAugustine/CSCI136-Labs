import StdDraw
import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Sierpinski:
    def __init__(self):
        self.points = {
            "x" : [],
            "y" : []}
        self.drawTriangleOutline()

    def drawTriangleOutline(self):
        x = 0
        y = 0
        s = 1
        b = math.sqrt(s**2 - (s/2)**2)
        point1 = Point(x, y)
        point2 = Point(x+s, y)
        point3 = Point(x+(s/2), b)
        self.points['x'] = [point1.x, point2.x, point3.x]
        self.points['y'] = [point1.y, point2.y, point3.y]
        StdDraw.setPenColor(StdDraw.LIGHT_GRAY)
        StdDraw.setPenRadius(.001)
        StdDraw.polygon(self.points['x'], self.points['y'])
        # StdDraw.show(2000)

    #
    # Draws a filled triangle
    #
    # Input: float x: vertex x point
    # Input: float y: vertex y point
    # Input: float s: side length of triangle
    #
    def filledTriangle(self, x, y, s):
        self.getPoints(x, y, s)
        StdDraw.filledPolygon(self.points['x'], self.points['y'])
        # StdDraw.show(2000)

    def getPoints(self, x, y, s):
        point1 = Point(x, y)
        # topY = math.sqrt(s**2 - (x+(s/2) - point1.x)**2) + point1.y
        b = math.sqrt(s**2 - (s/2)**2)
        point2 = Point(x+(s/2), b)
        point3 = Point(x-(s/2), b)
        self.points['x'] = [point1.x, point2.x, point3.x]
        self.points['y'] = [point1.y, point2.y, point3.y]

    # Draws a filled triangle
    #
    # Input: int n: depth remaining
    # Input: float x: vertex x point
    # Input: float y: vertex y point
    # Input: float s: side length of triangle
    #
    def sierpinski(self, n, x, y, s):
        if n == 0:
            self.filledTriangle(x, y, s)
            return
        b = math.sqrt(s**2 - (s/2)**2)
        # topY = math.sqrt(s**2 - (x+(s/2) - x)**2) + y
        self.sierpinski(n-1, x+(s/2), y, s/2)
        self.sierpinski(n-1, x-(s/2), y, s/2)
        self.sierpinski(n-1, x, b, s/2)

    
if __name__ == "__main__":
    StdDraw.clear()
    if (len(sys.argv) < 2):
        print("\nERROR: Sierpinski.py takes one command line argument: depth\n")
    else:
        depth = int(sys.argv[1])
        s = Sierpinski()
        StdDraw.setPenColor(StdDraw.BLACK)
        s.sierpinski(depth, .5, 0, 1)
        StdDraw.show(50000)
