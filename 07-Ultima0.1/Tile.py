#
# Author: Will Augustine
#
# Description: Contains the Tile class which is used to represent each tile in the world
#

# Imports
from enum import Enum # Imports Enum class from enum library
from picture import Picture as pic # Imports Picture class from picture as variable 'pic'
import StdDraw # Imports StdDraw to draw tiles

# Enumeration class to handle different tile types
class TileType(Enum):
    INVALID = None
    FLOOR = {'filename': 'brickfloor.gif', 'opaque': False, 'passable': True} # For code 'B'
    LAVA = {'filename': 'lava.gif', 'opaque': False, 'passable': True} # For code 'L'
    WATER = {'filename': 'water.gif', 'opaque': False, 'passable': False} # For code 'W'
    FOREST = {'filename': 'forest.gif', 'opaque': True, 'passable': True} # For code 'F'
    GRASS = {'filename': 'grasslands.gif', 'opaque': False, 'passable': True} # For code 'G'
    MOUNTAIN = {'filename': 'mountains.gif', 'opaque': True, 'passable': False} # For code 'M'
    WALL = {'filename': 'stonewall.gif', 'opaque': True, 'passable': False} # For code 'S'

# Class that handles all data and operations on tiles
class Tile:

    SIZE = 16 # Variable for the pixel size of each tile

    #
    # Description: Constructor for the Tile class
    # 
    # Inputs:
    #   char code: The code that represents a tile
    #
    # Outputs:
    #   N/A
    #
    def __init__(self, code):
        self.size = 16 # Variable for the pixel size of a tile
        self.code = code # Variable for the code inputtd
        self.lit = False # Sets default lit value as False
        self.isLava = False
        self.attributes = TileType.INVALID.value # Gets the attributes from INVALID as default
        if self.code == 'B': # If the inputted code was 'B'
            self.attributes = TileType.FLOOR.value # Set the attributes to dictionary of FLOOR in the enumeration class
        elif self.code == 'L': # If the inputted code was 'L'
            self.attributes = TileType.LAVA.value # Set the attributes to dictionary of LAVA in the enumeration class
            self.isLava = True
        elif self.code == 'W': # If the inputted code was 'W'
            self.attributes = TileType.WATER.value # Set the attributes to dictionary of WATER in the enumeration class
        elif self.code == 'F': # If the inputted code was 'F'
            self.attributes = TileType.FOREST.value # Set the attributes to dictionary of FOREST in the enumeration class
        elif self.code == 'G': # If the inputted code was 'G'
            self.attributes = TileType.GRASS.value # Set the attributes to dictionary of GRASS in the enumeration class
        elif self.code == 'M': # If the inputted code was 'M'
            self.attributes = TileType.MOUNTAIN.value # Set the attributes to dictionary of MOUNTAIN in the enumeration class
        elif self.code == 'S': # If the inputted code was 'S'
            self.attributes = TileType.WALL.value # Set the attributes to dictionary of WALL in the enumeration class
            

    #
    # Description: Returns if a tile is lit
    # 
    # Inputs:
    #   None 
    #
    # Outputs:
    #   Boolean value of if a tile is lit
    #
    def getLit(self):
        return self.lit # Returns a tile's lit value

    #
    # Description: Sets a tile's lit value based on inputted value
    # 
    # Inputs:
    #   boolean value: What state you want the tile's lit value to be
    #
    # Outputs:
    #   None
    #
    def setLit(self, value):
        self.lit = value # Set tile's lit value to inputted value

    #
    # Description: Returns if a tile is opaque (light does NOT pass through)
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   Boolean value of if a tile is opaque
    #
    def isOpaque(self):
        return self.attributes['opaque'] # Gets opaque value from tile's attributes

    #
    # Description: Returns if a tile is passable (can walk through it)
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   Boolean value of if a tile is passable
    #
    def isPassable(self):
        return self.attributes['passable'] # Gets passable value from tile's attributes

    #
    # Description: Draws the tile at the inputted location
    # 
    # Inputs:
    #   int x: x position of tile
    #   int y: y position of tile
    #
    # Outputs:
    #   None
    #
    def draw(self, x, y):
        x = x*self.size + self.size/2 # Convert x position into pixel location
        y = y*self.size + self.size/2 # Convert y position into pixel location
        if self.lit: # If the tile is lit
            tile = pic(self.attributes['filename']) # Create picture object based on filename specified in attributes
            StdDraw.picture(tile, x, y) # Draw the tile
        else: # If the tile is not lit
            tile = pic('blank.gif') # Create picture object based on blank image
            StdDraw.picture(tile, x, y) # Draw the tile

    #
    # Description: Returns the amount of damage the a tile deals
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   1: If tile is lava
    #   0: If tile is not lava
    #
    def getDamage(self):
        if self.isLava:
            return 1
        return 0
#
# Main code for testing the Tile class
#
if __name__ == "__main__":
    # Set up test parameters
    SIZE 	= 16
    WIDTH 	= 7
    HEIGHT 	= 2

    # Set up a StdDraw canvas on which to draw the tiles
    StdDraw.setCanvasSize(WIDTH * SIZE, HEIGHT * SIZE)
    StdDraw.setXscale(0.0, WIDTH * SIZE)
    StdDraw.setYscale(0.0, HEIGHT * SIZE)

    # Create a list of codes to test tile creation
    codes = ["B", "L", "W", "F", "G", "M", "S"]
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            tile = Tile(codes[i])
            # Light every second tile
            if (i + j) % 2 == 0:
                tile.setLit(True)
            print("%d %d : lit %s\topaque %s\tpassable %s" %(i, j, tile.getLit(), tile.isOpaque(), tile.isPassable()))
            tile.draw(i, j)
    StdDraw.show(5000)
