
#
# Author: Will Augustine
#   Username: waugustine
#
# Decription: Uses recursion, given the input, to draw colorful circles. Does
#   recursion to the level as the input is.
#


import StdDraw
import sys
import random
import color


# Changes the pen color to a random color every time the function is called
def setColor():
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    StdDraw.setPenColor(color.Color(color1, color2, color3))

    
# Given the center point and radius of a circle, it figures out the new center 
#   points to be able to draw circles touching the top, right, bottom, and left
#   of the current circle
#
# Takes the inputs n (how deep of recursion is left to execute), x (x position
#   for the center), y (y position for the center), and r (radius of the circle)
def lotsOfCircles(n, x, y, r):
    # States a minimum so the loop isn't infinte
    if n == 0:
        return
    # Calculates the center point for top circle
    xT = x
    yT = y + r

    # Calculates the center point for right circle
    xR = x + r
    yR = y

    # Calculates the center point for bottom circle
    xB = x
    yB = y - r

    # Calculates the center point for left circle
    xL = x - r
    yL = y

    # Calls setColor function and draws the top cirle with that color
    setColor()
    StdDraw.filledCircle(xT, yT, r)
    StdDraw.show(100)

    # Calls setColor function and draws the right cirle with that color
    setColor()
    StdDraw.filledCircle(xR, yR, r)
    StdDraw.show(100)

    # Calls setColor function and draws the bottom cirle with that color
    setColor()
    StdDraw.filledCircle(xB, yB, r)
    StdDraw.show(100)

    # Calls setColor function and draws the left cirle with that color
    setColor()
    StdDraw.filledCircle(xL, yL, r)
    StdDraw.show(100)

    # Runs the new points through the lotsOfCircles function
    lotsOfCircles(n-1, xT, yT, r/2)
    lotsOfCircles(n-1, xR, yR, r/2)
    lotsOfCircles(n-1, xB, yB, r/2)
    lotsOfCircles(n-1, xL, yL, r/2)

# Test code for the program 
if __name__ == "__main__":
    n = int(sys.argv[1])
    if n == 1:
        n = 0
    # Draws the background black filled circle
    StdDraw.filledCircle(.5, .5, .5)
    # Starts the function lotsOfCircles
    lotsOfCircles(n, .5, .5, .25)
    StdDraw.show(5000)
