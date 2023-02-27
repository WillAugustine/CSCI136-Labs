#
# Author: Will Augustine
#
# Description: 
#

from enum import Enum, auto
from picture import Picture as pic
import StdDraw

#Enumeration class to handle different tile types
class TileType(Enum):
    INVALID = None
    FLOOR = {'filename': 'brickfloor.gif', 'opaque': False, 'passable': True}
    LAVA = {'filename': 'lava.gif', 'opaque': False, 'passable': True}
    WATER = {'filename': 'water.gif', 'opaque': False, 'passable': False}
    FOREST = {'filename': 'forest.gif', 'opaque': True, 'passable': True}
    GRASS = {'filename': 'grasslands.gif', 'opaque': False, 'passable': True}
    MOUNTAIN = {'filename': 'mountains.gif', 'opaque': True, 'passable': False}
    WALL = {'filename': 'stonewall.gif', 'opaque': True, 'passable': False}

# Class that handles all data and operations on tiles
class Tile:

    # Constructor for a tile
    #
    # Paramter is a string or character that specifies the
    #   type of tile
    def __init__(self, code):
        self.size = 16
        self.code = code
        self.lit = False
        self.attributes = TileType.INVALID.value
        if self.code == 'B':
            self.attributes = TileType.FLOOR.value
        elif self.code == 'L':
            self.attributes = TileType.LAVA.value
        elif self.code == 'W':
            self.attributes = TileType.WATER.value
        elif self.code == 'F':
            self.attributes = TileType.FOREST.value
        elif self.code == 'G':
            self.attributes = TileType.GRASS.value
        elif self.code == 'M':
            self.attributes = TileType.MOUNTAIN.value
        elif self.code == 'S':
            self.attributes = TileType.WALL.value
            

    # Accessor for the lit instance variable
    #
    # Returns a True if the tile is lit, False otherwise
    def getLit(self):

        return self.lit

    # Mutator for the lit instance variable
    #
    # Input parament value is a boolean variable
    def setLit(self, value):

        self.lit = value
        pass

    # Does light pass through this tile
    #
    # Returns True if the tile is opaque, False otherwise
    def isOpaque(self):

        return self.attributes['opaque']

    # Can the hero walk through this tile
    #
    # Returns True if the tile can be moved through,
    #    False otherwise
    def isPassable(self):

        return self.attributes['passable']

    # Draw the tile at the given location
    #
    # Input parameters x and y are integers specifying
    #    the tile's position within the world grid
    def draw(self, x, y):
        x = x*self.size + self.size/2
        y = y*self.size + self.size/2
        if self.lit:
            tile = pic(self.attributes['filename'])
            StdDraw.picture(tile, x, y)
        else:
            tile = pic('blank.gif')
            StdDraw.picture(tile, x, y)

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
