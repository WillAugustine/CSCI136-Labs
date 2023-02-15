import StdDraw
import sys
import math

def sierpinski(depth, x, y, size):
    if depth == 0:
        # Base case: draw a triangle
        StdDraw.filledPolygon([x, x + size/2, x + size], [y, y + size, y])
    else:
        # Recursive case: draw three triangles
        sierpinski(depth-1, x, y, size/2)
        sierpinski(depth-1, x + size/2, y, size/2)
        sierpinski(depth-1, x + size/4, y + size/2, size/2)

# # Set up the canvas
# StdDraw.setCanvasSize(600, 600)
# StdDraw.setXscale(0, 1)
# StdDraw.setYscale(0, 1)
# StdDraw.setPenColor(StdDraw.BLUE)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Call Sierpinski.py with the command line argument 'depth'!")
    else:
        StdDraw.setPenColor(StdDraw.BLACK)
        depth = int(sys.argv[1])
        # Call the recursive function to draw the Sierpinski triangle
        b = math.sqrt(1**2 - (1/2)**2)
        sierpinski(depth, 0, 0, b)

        # Show the final result
        StdDraw.show()
