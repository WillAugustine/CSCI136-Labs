#
# Author: Will Augustine
#
# Description: Draws and modifies the world for the Ultima game
#

# Imports
from Tile import Tile # Imports Tile class from Tile.py
from Avatar import Avatar # Imports Avatar class from Avatar.py
import sys # Imports sys for reading in command line arguments
import StdDraw # Imports StdDraw for drawing world

class World:

    #
    # Description: Constructor for the World class
    # 
    # Inputs:
    #   string filename: the file you want to read in
    #
    # Outputs:
    #   N/A
    #
    def __init__(self, filename):
        fileReader = open(filename, 'r') # Variable for all input file information
        fileContents = fileReader.read().splitlines() # Array of strings from input file
        self.width = int(fileContents[0].split()[0]) # Get the width from the first line
        self.height = int(fileContents[0].split()[1]) # Get the height from the first line
        self.maxY = self.height - 1 # Set maxY value (since height does not account for starting at 0)
        self.avatarX = int(fileContents[1].split()[0]) # Variable for avatar's x position
        self.avatarY = int(fileContents[1].split()[1]) # Variable for avatar's y position
        self.avatar = Avatar(self.avatarX, self.avatarY) # Variable for object of avatar class (want the same avatar througout the game)
        self.world = [[0 for i in range(self.width)] for j in range(self.height)] # Variable for world of Tile class object
        # Loop to extract world character, create Tile object from character, then add Tile object
        #   to the self.world variable in the correct spot
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
        self.world = list(reversed(self.world)) # Reverses the world
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
            return True if self.world[self.avatarY + 1][self.avatarX].isPassable() else False
        if (direction == 'down'): # If specified direction is down   
            return True if self.world[self.avatarY - 1][self.avatarX].isPassable() else False
        if (direction == 'left'): # If specified direction is left
            return True if self.world[self.avatarY][self.avatarX - 1].isPassable() else False
        if (direction == 'right'): # If specified direction is right
            return True if self.world[self.avatarY][self.avatarX + 1].isPassable() else False

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
        self.avatarX = self.avatar.getX() # Updates self.avatarX with current avatar x
        self.avatarY = self.avatar.getY() # Updates self.avatarY with current avatar y
        
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
        if (ch == 'w') & (self.avatarY < self.height): # If the player clicked 'w' and the move is within bounds
            if self.canMoveAvatar('up'): # See if the above block is passable
                self.moveAvatar('up') # If the block is passable, move the avatar up

        elif (ch == 's') & (self.avatarY > 0): # If the player clicked 's' and the move is within bounds
            if self.canMoveAvatar('down'): # See if the below block is passable
                self.moveAvatar('down') # If the block is passable, move the avatar down

        elif (ch == 'a') & (self.avatar.getX() > 0): # If the player clicked 'a' and the move is within bounds
            if self.canMoveAvatar('left'): # See if the left block is passable
                self.moveAvatar('left') # If the block is passable, move the avatar left

        elif (ch == 'd') & (self.avatar.getX() < self.width): # If the player clicked 'd' and the move is within bounds
            if self.canMoveAvatar('right'): # See if the right block is passable
                self.moveAvatar('right') # If the block is passable, move the avatar right

        elif (ch == '+'): # If the player clicked '+'
            self.avatar.increaseTorch() # Increase the torch radius

        elif (ch == '-'): # If the player clicked '-'
            self.avatar.decreaseTorch() # Decrease the torch radius
            
        
    
    #
    # Description: Draws the world
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   None
    #
    def draw(self):
        self.setLit(False) # Sets all tiles to unlit
        yCounter = 0 # Counter for row position in self.world
        self.light(self.avatarX, self.avatarY, self.avatar.getTorchRadius()) # Lights tiles around avatar based on torch radius
        for colNum in range(self.height): # Traverse through the column index
            for rowNum in range(self.width): # For each index (row) in each column
                self.world[colNum][rowNum].draw(rowNum, colNum) # Draw the current tile
        self.avatar.draw() # Draw the avatar on top of the tiles
    
    #
    # Description: Calls lightDFS to light up tiles based on opaque values and torch radius
    # 
    # Inputs:
    #   int x: Avatar's x position
    #   int y: Avatar's y position
    #   float r: radius of the Avatar's torch 
    #
    # Outputs:
    #   Number of tiles lit
    #
    def light(self, x, y, r):
        # self.world[self.maxY - y][x].setLit(True) # Sets the Avatar's position as lit
        # litTiles = 1 # Set number of lit tiles to 1 since Avatar's position is lit
        litTiles = self.lightDFS(x, y, x, y, r) # Calls lightDFS to light surrounding area and adds number of tiles lit to litTiles
        return litTiles # Returns the number of tiles lit by lightDFS

    #
    # Description: A recursive function to light up nearby tiles based on torch strength
    # 
    # Inputs:
    #   int x: Avatar's x position
    #   int y: Avatar's y position
    #   int currX: The current x position being looked at
    #   int currY: The current y position being looked at
    #   float r: radius of the Avatar's torch 
    #
    # Outputs:
    #   Number of tiles lit
    #
    def lightDFS(self, x, y, currentX, currentY, r):
        dist = ((currentX - x)**2 + (currentY - y)**2)**0.5 # Calculates the distance from avatar to current position
        
        litTiles = 0 # Set litTiles equal to 0 since no tiles are lit yet
        '''
            if currentX is within bounds and
            currentY is within bounds and
            the current tile is not lit and
            distance from tile to avatar is less than torch radius
        '''
        if ((currentX == x) and (currentY == y)):
            self.world[currentY][currentX].setLit(True)
            litTiles += 1
        elif currentX in range(self.width) and \
            currentY in range(self.height) and \
            not self.world[currentY][currentX].getLit() and \
            dist < r:
            
            if (self.world[currentY][currentX].isOpaque() == True): # If a block is opaque (you cannot see through it)
                self.world[currentY][currentX].setLit(True) # Set the tile as lit
                return 1 # Do not light any more tiles after opaque tile
            self.world[currentY][currentX].setLit(True) # Set the tile as lit
            litTiles += 1 # Increment number of tiles lit
        else: # Base case
            return 0 # Return 0 since no tiles were lit this go around
        litTiles += self.lightDFS(x, y, currentX-1, currentY, r) # Light the tile to the left
        litTiles += self.lightDFS(x, y, currentX, currentY-1, r) # Light the tile above
        litTiles += self.lightDFS(x, y, currentX+1, currentY, r) # Light the tile to the right
        litTiles += self.lightDFS(x, y, currentX, currentY+1, r) # Light the tile below
        return litTiles # Return the number of tiles lit

    #
    # Description: Sets all tiles in the world to a specified lit value
    # 
    # Inputs:
    #   boolean value: The desired lit value for all tiles in the world
    #
    # Outputs:
    #   None
    #
    def setLit(self, value):

        for row in self.world: # For each row in the world 
            for tile in row: # For each tile in the current row
                tile.setLit(value) # Set the lit value equal to the inputted value
    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    # StdDraw.show()
