#
# Author: Will Augustine
#
# Description: Draws and modifies the world for the Ultima game
#

# Imports
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
        fileReader = open(filename, 'r') # Variable for all input file information
        fileContents = fileReader.read().splitlines() # Array of strings from input file
        self.width = int(fileContents[0].split()[0]) # Get the width from the first line
        self.height = int(fileContents[0].split()[1]) # Get the height from the first line
        self.maxY = self.height - 1 # Set maxY value (since height does not account for starting at 0)
        self.avatarX = int(fileContents[1].split()[0]) # Variable for avatar's x position
        self.avatarY = int(fileContents[1].split()[1]) # Variable for avatar's y position
        self.avatar = Avatar(self.avatarX, self.avatarY) # Variable for object of avatar class (want the same avatar througout the game)
        self.world = [[0 for i in range(self.width)] for j in range(self.height)] # Variable for world of Tile class objects
        #
        # Loop to extract world character, create Tile object from character, then add Tile object
        #   to the self.world variable in the correct spot
        #
        worldX = 0 # Counter for x position
        for line in fileContents: # For each row
            if worldX < 2: # Ignores the first two rows in input file
                pass
            else:
                worldY = 0 # Counter for y position
                for tile in line.split(): # For each character in the row
                    self.world[worldX-2][worldY] = Tile(tile) # Add Tile object to self.world
                    worldY += 1 # Increment y position counter
            worldX += 1 # Increment x position counter
        self.size = 16 # Variable for the size of a tile
        # Set up a StdDraw canvas on which to draw the tiles
        StdDraw.setCanvasSize(self.width * self.size, self.height * self.size)
        StdDraw.setXscale(0.0, self.width * self.size)
        StdDraw.setYscale(0.0, self.height * self.size)

    #
    # Description: Used to determine if the avatar can move in the specified direction
    # 
    # Inputs:
    #   string direction: Either 'up', 'down', 'right', or 'left'
    # 
    # Outputs:
    #   True: if the avatar can move in the specified direction    
    #   False: if the avatar can NOT move in the specified direction
    #
    def canMoveAvatar(self, direction):
        if (direction ==  'up'): # If specified direction is up
            return True if self.world[self.maxY - self.avatarY - 1][self.avatarX].isPassable() else False
        if (direction == 'down'): # If specified direction is down   
            return True if self.world[self.maxY - self.avatarY + 1][self.avatarX].isPassable() else False
        if (direction == 'left'): # If specified direction is left
            return True if self.world[self.maxY - self.avatarY][self.avatarX - 1].isPassable() else False
        if (direction == 'right'): # If specified direction is right
            return True if self.world[self.maxY - self.avatarY][self.avatarX + 1].isPassable() else False

    #
    # Description: Used to move the avatar in the specified direction
    # 
    # Inputs:
    #   string direction: Either 'up', 'down', 'right', or 'left'
    # 
    # Outputs:
    #   None
    #
    def moveAvatar(self, direction):
        if (direction ==  'up'): # If specified direction is up
            self.avatar.setLocation(self.avatar.getX(), self.avatar.getY() + 1)
        if (direction == 'down'): # If specified direction is down       
            self.avatar.setLocation(self.avatar.getX(), self.avatar.getY() - 1)
        if (direction == 'left'): # If specified direction is left
            self.avatar.setLocation(self.avatar.getX() - 1, self.avatar.getY())
        if (direction == 'right'): # If specified direction is right
            self.avatar.setLocation(self.avatar.getX() + 1, self.avatar.getY())
        
    #
    # Description: Handles a key pressed and either moves the avatar or modifies torch brightness
    # 
    # Inputs:
    #   char ch: The key that was pressed
    # 
    # Outputs:
    #   None
    #
    def handleKey(self, ch):
        self.avatarX = self.avatar.getX()
        self.avatarY = self.avatar.getY()
        if (ch == 'w') & (self.avatarY < self.height):
            if self.canMoveAvatar('up'):
                self.moveAvatar('up')

        elif (ch == 's') & (self.avatarY > 0):
            if self.canMoveAvatar('down'):
                self.moveAvatar('down')

        elif (ch == 'a') & (self.avatar.getX() > 0):
            if self.canMoveAvatar('left'):
                self.moveAvatar('left')

        elif (ch == 'd') & (self.avatar.getX() < self.width):
            if self.canMoveAvatar('right'):
                self.moveAvatar('right')

        elif (ch == '+'):
            self.avatar.increaseTorch()

        elif (ch == '-'):
            self.avatar.decreaseTorch()
        self.draw()
            
        
    
    # Draw all the lit tiles
    #
    # Only action is to draw all the components associated with the world
    def draw(self):
        self.setLit(False)
        yCounter = 0
        self.light(self.avatar.getX(), self.avatar.getY(), self.avatar.getTorchRadius())
        for row in self.world:
            tileX = 0
            for tile in row:
                tileY = self.maxY - yCounter
                tile.draw(tileX, tileY)
                tileX += 1
            yCounter +=1
        self.avatar.draw()
    
    # Light the world
    #
    # Input parameters are the x and y position of the avatar and the
    #    current radius of the torch.
    #    Calls the recursive lightDFS method to continue the lighting
    # Returns the total number of tiles lit
    def light(self, x, y, r):
        self.world[self.maxY - y][x].setLit(True)
        litTiles = self.lightDFS(x, y, x, y, self.avatar.getTorchRadius())
        return litTiles
    
    # Recursively light from (x, y) limiting to radius r
    #
    # Input parameters are (x,y), the position of the avatar,
    #    (currX, currY), the position that we are currently looking
    #    to light, and r, the radius of the torch.
    # Returns the number of tiles lit
    def lightDFS(self, x, y, currX, currY, r):
        dist = ((currX - x)**2 + (currY - y)**2)**0.5
        if dist <= r:
            self.world[self.maxY - currY][currX].setLit(True)
            litTiles = 1
            if not ((x==currX) and (y==currY)):
                if (self.world[self.maxY - currY][currX].isOpaque() == True):
                    return litTiles
            if ((currX > 0) and (currX <= x)):
                litTiles += self.lightDFS(x, y, currX-1, currY, r)
            if ((currY > 0) and (currY <= y)):
                litTiles += self.lightDFS(x, y, currX, currY-1, r)
            if ((currX < self.width) and (currX >= x)):
                litTiles += self.lightDFS(x, y, currX+1, currY, r)
            if ((currY < self.maxY) and (currY >= y)):
                litTiles += self.lightDFS(x, y, currX, currY+1, r)
            return litTiles
        return 0
            
    # Turn all the lit values of the tiles to a given value. Used
    #    to reset lighting each time the avatar moves or the torch
    #    strength changes
    #
    # Input paramter is a boolean value, generally False, to turn off
    #    the light, but is flexible to turn the light on in some future
    #    version
    def setLit(self, value):

        for column in self.world:
            for tile in column:
                tile.setLit(value)
    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    # StdDraw.show()
