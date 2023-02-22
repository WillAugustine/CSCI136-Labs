#
# Author: Will Augustine        
#
# Description: World class that holds all information about tiles and
#              characters in the Ultima 0.0 game

from Tile import Tile
from Avatar import Avatar
import math
import sys
import StdDraw

class World:

    # Constructor for the world
    #
    # Input parameter is a file name holding the configuration information
    #    for the world to be created
    #    The constructor reads in file data, stores it in appropriate
    #    attributes and sets up the window within which to draw.
    #    It also initializes the lighting in the world.
    def __init__(self, filename):
        with open(filename, 'r') as f:
            # Read in the first line of text
            line = f.readline().split()
            # Translate that line to width and height
            self.width = int(line[0])
            self.height = int(line[1])
            # Read in the second line of text
            line = f.readline().split()
            # Translate that into the avatar position
            self.avatar = Avatar(int(line[0]), int(line[1]), int(line[2]), int(line[3]), float(line[4]))
            self.tiles = [[None for i in range(self.height)] for j in range(self.width)]
            # Read in the rest of the file and parse into color blocks
            line = f.read().split()
            index = 0
            for i in range(0, self.height):
                for j in range(0, self.width):
                    self.tiles[j][self.height - i - 1] = Tile(line[index])
                    index += 1
            f.close()                             

        # Set up the window for drawing
        StdDraw.setCanvasSize(self.width * Tile.SIZE, self.height * Tile.SIZE)
        StdDraw.setXscale(0.0, self.width * Tile.SIZE)
        StdDraw.setYscale(0.0, self.height * Tile.SIZE)

        # Initial lighting
        self.light(self.avatar.getX(), self.avatar.getY(), self.avatar.getTorchRadius())
        self.draw()

    # Accept keyboard input and performs the appropriate action
    # 
    # Input parameter is a character that indicates the action to be taken
    def handleKey(self, ch):
        deltaX = 0
        
        deltaY = 0
        if ch == 'w':
            deltaY = 1
        elif ch == 's':
            deltaY = -1
        elif ch == 'a':
            deltaX = -1
        elif ch == 'd':
            deltaX = 1
        elif ch == '+':
            self.avatar.increaseTorch()
        elif ch == '-':
            self.avatar.decreaseTorch()

        # If the keyboard input was to move avatar
        if deltaX != 0 or deltaY != 0:
            x = self.avatar.getX() + deltaX
            y = self.avatar.getY() + deltaY

            if x >= 0 and x < self.width and \
               y >= 0 and y < self.height and \
               self.tiles[x][y].isPassable():
                # New location is in bounds and passable
                self.avatar.setLocation(x, y)
        self.setLit(False)
        self.light(self.avatar.getX(), self.avatar.getY(), self.avatar.getTorchRadius())
    
    # Draw all the lit tiles
    #
    # Only action is to draw all the components associated with the world
    def draw(self):
        # First update the lighting of the world
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[x][y].draw(x, y)
        self.avatar.draw()

    # Light the world
    #
    # Input parameters are the x and y position of the avatar and the
    #    current radius of the torch.
    #    Calls the recursive lightDFS method to continue the lighting
    # Returns the total number of tiles lit
    def light(self, x, y, r):
        result = self.lightDFS(x, y, x, y, r)
        print("light(%d, %d, %.1f) = %d" %(x, y, r, result))
        return result
    
    # Recursively light from (x, y) limiting to radius r
    #
    # Input parameters are (x,y), the position of the avatar,
    #    (currX, currY), the position that we are currently looking
    #    to light, and r, the radius of the torch.
    # Returns the number of tiles lit
    def lightDFS(self, x, y, currentX, currentY, r):
        if currentX < 0 or currentY < 0 or \
           currentX >= self.width or currentY >= self.height or \
           self.tiles[currentX][currentY].getLit():
                return 0
        
        result = 0
        deltaX = x - currentX
        deltaY = y - currentY
        
        dist = math.sqrt(deltaX * deltaX + deltaY * deltaY)

        if dist < r:
            self.tiles[currentX][currentY].setLit(True)
            result += 1
                                                            
            if not self.tiles[currentX][currentY].isOpaque():
                result += self.lightDFS(x, y, currentX - 1, currentY, r)	# west		
                result += self.lightDFS(x, y, currentX + 1, currentY, r)	# east
                result += self.lightDFS(x, y, currentX, currentY - 1, r)	# north
                result += self.lightDFS(x, y, currentX, currentY + 1, r)	# south							
        return result
            
    # Turn all the lit values of the tiles to a given value. Used
    #    to reset lighting each time the avatar moves or the torch
    #    strength changes
    #
    # Input paramter is a boolean value, generally False, to turn off
    #    the light, but is flexible to turn the light on in some future
    #    version
    def setLit(self, value):
        for x  in range(0, self.width):
            for y in range(0, self.height):
                self.tiles[x][y].setLit(value)


    # Function to see if the avatar is still alive
    #
    #
    # Reads to see if avatar hit points aren't 0
    def avatarAlive(self):
        if self.avatar.getHitPoints() != 0:
            return True
        else:
            return False

    # Function to determine if a monster can move to a certain spot
    def monsterMove(self, x, y, monster):
        if x > self.width or \
           x < 0 or \
           y > self.height or \
           y < 0:
            return
        
    # Function to determine if an avatar can move to a certain spot
    def avatarMov1e(self, x, y):
        if x > self.width or \
           x < 0 or \
           y > self.height or \
           y < 0:
            return

    # Function to determine how many monsters are left
    def getNumMonsters(self):
        return 1
    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    StdDraw.show()
