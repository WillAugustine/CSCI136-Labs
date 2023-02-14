import StdDraw
import sys

def htree(n, size, x, y, c):
    if n == 0:
        return
      
    x0 = x - size/2;       # left side of the H
    x1 = x + size/2;       # right side of the H
    y0 = y - size/2;       # bottom most part of the H
    y1 = y + size/2;       # top most part of the H
      
    StdDraw.setPenColor(c)
    
    StdDraw.line(x0,  y, x1,  y); # draw the horizontal center of the H
    StdDraw.line(x0, y0, x0, y1); # draw the left leg of the H
    StdDraw.line(x1, y0, x1, y1); # draw the right leg of the H
    
    StdDraw.show(0);
      
    htree(n-1, size/2, x1, y1, StdDraw.BLACK);    # upper-right
    htree(n-1, size/2, x0, y0, StdDraw.DARK_GRAY);    # lower-left
    htree(n-1, size/2, x0, y1, StdDraw.GRAY);    # upper-left
    htree(n-1, size/2, x1, y0, StdDraw.LIGHT_GRAY);    # lower-right

# Test code to run Htree
if __name__ == "__main__":
      n = int(sys.argv[1])
      StdDraw.setPenRadius(.001)
      htree(n, .5, .5, .5, StdDraw.BLACK)
      
      # Delay 10 seconds at the end to view the figure.
      StdDraw.show(10000)
