#
# Author: 
#
# Description: 
#

from enum import Enum, auto
import picture
import StdDraw

#Enumeration class to handle different tile types
class TileType(Enum):
    INVALID = auto()
    FLOOR = auto()
    LAVA = auto()
    WATER = auto()
    FOREST = auto()
    GRASS = auto()
    MOUNTAIN = auto()
    WALL = auto()

# Class that handles all data and operations on tiles
class Tile:
    # Static variable associated with tiles to specity the size
    SIZE = 16

    # Constructor for a tile
    #
    # Paramter is a string or character that specifies the
    #   type of tile
    def __init__(self, code):

        ##### YOUR CODE HERE #####
        pass

    # Accessor for the lit instance variable
    #
    # Returns a True if the tile is lit, False otherwise
    def getLit(self):

        ##### YOUR CODE HERE #####
        pass

    # Mutator for the lit instance variable
    #
    # Input parament value is a boolean variable
    def setLit(self, value):

        ##### YOUR CODE HERE #####
        pass

    # Does light pass through this tile
    #
    # Returns True if the tile is opaque, False otherwise
    def isOpaque(self):

        ##### YOUR CODE HERE #####
        pass

    # Can the hero walk through this tile
    #
    # Returns True if the tile can be moved through,
    #    False otherwise
    def isPassable(self):

        ##### YOUR CODE HERE #####
        pass

    # Draw the tile at the given location
    #
    # Input parameters x and y are integers specifying
    #    the tile's position within the world grid
    def draw(self, x, y):

        ##### YOUR CODE HERE #####
        pass

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
