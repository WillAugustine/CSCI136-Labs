#
# Author: Will Augustine
#
# Description:
#

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
        fileReader = open(filename, 'r')
        fileContents = fileReader.read().splitlines()
        self.width = int(fileContents[0].split()[0])
        self.height = int(fileContents[0].split()[1])
        self.avatarX = int(fileContents[1].split()[0])
        self.avatarY = int(fileContents[1].split()[1])
        self.avatar = Avatar(self.avatarX, self.avatarY)
        self.world = [[0 for i in range(self.width)] for j in range(self.height)]
        worldX = 0
        for line in fileContents:
            if worldX < 2:
                pass
            else:
                worldY = 0
                for tile in line.split():
                    self.world[worldX-2][worldY] = Tile(tile)
                    worldY += 1
            worldX += 1

        # Set up test parameters
        self.size = 16
        # Set up a StdDraw canvas on which to draw the tiles
        StdDraw.setCanvasSize(self.width * self.size, self.height * self.size)
        StdDraw.setXscale(0.0, self.width * self.size)
        StdDraw.setYscale(0.0, self.height * self.size)

        

    # Accept keyboard input and performs the appropriate action
    # 
    # Input parameter is a character that indicates the action to be taken
    def handleKey(self, ch):
        # print(f"Key pressed: {ch}")
        if (ch == 'w') & (self.avatar.getY() < self.height):
            self.avatar.setLocation(self.avatar.getX(), self.avatar.getY() + 1)
        elif (ch == 's') & (self.avatar.getY() > 0):
            self.avatar.setLocation(self.avatar.getX(), self.avatar.getY() - 1)
        elif (ch == 'a') & (self.avatar.getX() > 0):
            self.avatar.setLocation(self.avatar.getX() - 1, self.avatar.getY())
        elif (ch == 'd') & (self.avatar.getX() < self.width):
            self.avatar.setLocation(self.avatar.getX() + 1, self.avatar.getY())
        elif (ch == '+'):
            self.avatar.increaseTorch()
        elif (ch == '-'):
            self.avatar.decreaseTorch()
        self.draw()
            
        
    
    # Draw all the lit tiles
    #
    # Only action is to draw all the components associated with the world
    def draw(self):
        yCounter = 0
        for row in self.world:
            tileX = 0
            for tile in row:
                tileY = self.height - yCounter - 1
                tile = Tile(tile)
                tile.setLit(True)
                tile.draw(tileX, tileY)
                tileX += 1
            yCounter +=1
        self.avatar.draw()

        # StdDraw.show()
    
    # Light the world
    #
    # Input parameters are the x and y position of the avatar and the
    #    current radius of the torch.
    #    Calls the recursive lightDFS method to continue the lighting
    # Returns the total number of tiles lit
    def light(self, x, y, r):

        avatarX = self.avatar.getX()
        avatarY = self.avatar.getY()
        return 0
    
    # Recursively light from (x, y) limiting to radius r
    #
    # Input parameters are (x,y), the position of the avatar,
    #    (currX, currY), the position that we are currently looking
    #    to light, and r, the radius of the torch.
    # Returns the number of tiles lit
    def lightDFS(self, x, y, currentX, currentY, r):

        if abs(x - currentX) > r:
            return 0
        if abs(y - currentY) > r:
            return 0
        # checking light to left
        if ((x - currentX) > 0):
            pass
        for i in range():
            pass
        return 0
            
    # Turn all the lit values of the tiles to a given value. Used
    #    to reset lighting each time the avatar moves or the torch
    #    strength changes
    #
    # Input paramter is a boolean value, generally False, to turn off
    #    the light, but is flexible to turn the light on in some future
    #    version
    def setLit(self, value):

        ##### YOUR CODE HERE #####
        pass
    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    # StdDraw.show()
