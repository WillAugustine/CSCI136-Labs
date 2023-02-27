# 
# Author: 
# 
# Description:
#

from enum import Enum, auto
import time
import StdDraw
import picture
import random
from Tile import Tile

class MonsterType(Enum):
    INVALID = auto()
    SKELETON = auto()
    ORC = auto()
    BAT = auto()
    SLIME = auto()

class Monster:

    # Construct a new monster
    # 
    # param world	- the world the monster moves about in
    # param code	- the string code that distinguishes types of monsters
    # param x		- the x position of the monster
    # param y		- the y position of the monster
    # param hp		- hit points - damage sustained by the monster
    # param damage	- damage the monster causes
    # param sleepMs	- delay between time monster moves
    def __init__(self, world, code, x, y, hp, damage, sleepMs):

        ##### YOUR CODE HERE #####
        pass

    # The avatar has attacked a monster!
    #
    # param points	- number of hit points to be subtracted from monster
    def incurDamage(self, points):

        ##### YOUR CODE HERE #####
        pass

    #
    # Draw this monster at its current location
    def draw(self):

        ##### YOUR CODE HERE #####
        pass

    #
    # Get the number of hit points the monster has ramaining
    # 
    # return the number of hit points
    def getHitPoints(self):

        ##### YOUR CODE HERE #####
        return 0

    #
    # Get the amount of damage a monster causes
    # 
    # return amount of damage monster causes
    def getDamage(self):

        ##### YOUR CODE HERE #####
        return 0

    #
    # Get the x position of the monster
    # 
    # return x position
    def getX(self):

        ##### YOUR CODE HERE #####
        return 0

    #
    # Get the y position of the monster
    # 
    # return y position
    def getY(self):

        ##### YOUR CODE HERE #####
        return 0

    #
    # Set the new location of the monster
    # 
    # param x the new x location
    # param y the new y location
    def setLocation(self, x, y):

        ##### YOUR CODE HERE #####
        pass

    #
    # Thread that moves the monster around periodically
    def run(self):

        ##### YOUR CODE HERE #####
        pass
