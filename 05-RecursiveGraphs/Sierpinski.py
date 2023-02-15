
#
# Author: Will Augustine
#
# Description: Uses recursion, given the input, to draw triangles. Does recursion
#       to the depth that the input is.
#

# Imports
import sys # Used for getting command line input
import StdDraw # Used for drawing polygons (triangles)
import math # Used for calculating square roots

#
# Class for easily reading and creating x and y points
#
class Point:

    #
    # Initializer function for Point class
    #
    # Inputs:
    #   float x: x value for a point - default = None
    #   float y: y value for a point - default = None
    #
    def __init__(self, x=None, y=None):
        self.x = x # Sets self.x equal to input x (default = None)
        self.y = y # Sets self.y equal to input y (default = None)


#
# Class for recursivly drawing Sierpinski triangles
#
class Recursion:

    #
    # Initializer function for Recursion class
    #
    # Inputs:
    #   None
    #
    def __init__(self):
        # Creates dictionary to store the three points for a triangle
        self.points = {
            'x': [],
            'y': []
        }
    
    #
    # Draws the outline triangle in gray and the initial center filled triangle in black 
    #
    # Inputs:
    #   Point point: bottom middle point of the initial middle triangle
    #   float s: side length of the initial middle triangle
    #
    def setupCanvas(self, point, s):
        x = [0, 1, 1/2] # x points for gray outline triangle
        y = [0, 0, (3**(1/2))/2] # y points for gray outline triangle

        StdDraw.setPenColor(StdDraw.GRAY) # Sets pen color to gray
        StdDraw.polygon(x, y) # Draws upright triangle outline
        StdDraw.setPenColor() # Changes pen color to default (black)
        
        self.filledTriangle(point.x, point.y, s) # Draws the initial triangle - cannot draw in sierpenski since there is only one   

    #
    # Gets the three points of a triangle based on bottom point
    #
    # Inputs:
    #   float x: x value for bottom point
    #   float y: y value for bottom point
    #   float s: side length for equalateral triangle
    #
    def getPoints(self, x, y, s):
        point1 = Point(x, y) # Creates Point class object for bottom middle point
        topY = y + math.sqrt((s**2) - (s/2)**2) # Calcualtion for top of triangle's y coordinate
        point2 = Point(x-(s/2), topY) # Creates Point class object for top left point
        point3 = Point(x+(s/2), topY) # Creates Point class object for top right point
        self.points['x'] = [point1.x, point2.x, point3.x] # Updates x values in self.points
        self.points['y'] = [point1.y, point2.y, point3.y] # Updates y values in self.points

    #
    # Draws a filled triangle based on bottom middle coordinates and side length
    #
    # Inputs:
    #   float x: x value for bottom point
    #   float y: y value for bottom point
    #   float s: side length for equalateral triangle
    #
    def filledTriangle(self, x, y, s):
        self.getPoints(x, y, s) # Updates self.points with all three points of triangle 
        StdDraw.filledPolygon(self.points['x'], self.points['y']) # Draws the filled triangle
        StdDraw.show(100) # Show each new triangle for 100 milliseconds
        
    #
    # Recursive function that calculates the left, right, and top triangle's bottom middle points
    #   and draws the triangles until depth has reached 0
    #
    # Inputs:
    #   int n: depth of recursion
    #   float x: x value for bottom point
    #   float y: y value for bottom point
    #   float s: side length for equalateral triangle
    #
    def sierpinski(self, n, x, y, s):
        if n == 0: # Base case - if depth equals 0
            return # exit the recursion loop
        
        topPoint = Point(x, y + math.sqrt(((2*s)**2) - (s**2))) # Creates the top triangle's bottom middle point
        leftPoint = Point(x-s, y) # Creates the left triangle's bottom middle point
        rightPoint = Point(x+s, y) # Creates the right triangle's bottom middle point

        self.filledTriangle(topPoint.x, topPoint.y, s) # Draws top triangle
        self.filledTriangle(leftPoint.x, leftPoint.y, s) # Draws left triangle
        self.filledTriangle(rightPoint.x, rightPoint.y, s) # Draws right triangle

        self.sierpinski(n-1, topPoint.x, topPoint.y, s/2) # Runs recursion for top triangle
        self.sierpinski(n-1, leftPoint.x, leftPoint.y, s/2) # Runs recursion for left triangle
        self.sierpinski(n-1, rightPoint.x, rightPoint.y, s/2) # Runs recursion for right triangle

if __name__ == "__main__":
    if len(sys.argv) < 2: # If missing the depth command line argument
        print("You need to add depth to the command line argument:")
        print("\t'python Sierpinski.py <depth>'")
        exit() # Exit program

    rec = Recursion() # Creates object of the Recursion class

    N = int(sys.argv[1]) # Gets the depth from command line

    initialPoint = Point(.5, 0) # Center triangle's bottom middle point
    s = .5 # Center triangle's side length

    rec.setupCanvas(initialPoint, s) # Sets up the canvas with outline and initial center triangle

    rec.sierpinski(N-1, initialPoint.x, initialPoint.y, s/2) # Since initial triangle is drawn, reduce size and depth and call sierpinski

    StdDraw.show() # Shows the final product until it is closed out (indefinitly)
