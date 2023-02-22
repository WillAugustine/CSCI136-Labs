# 
# Author: Will Augustine 
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

    SIZE = 16
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

        self.world = world
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.sleepMs = sleepMs
        if code == "SK":
            self.type = MonsterType.SKELETON
        elif code == "OR":
            self.type = MonsterType.ORC
        elif code == "SL":
            self.type = MonsterType.SLIME
        elif code == "BA":
            self.type = MonsterType.BAT
        else:
            self.type = MonsterType.INVALID
        pass

    # The avatar has attacked a monster!
    #
    # param points	- number of hit points to be subtracted from monster
    def incurDamage(self, points):
        self.hp -= points
        pass

    #
    # Draw this monster at its current location
    def draw(self):
        drawX = (self.x + 0.5) * self.SIZE
        drawY = (self.y + 0.5) * self.SIZE

        
        if self.type == MonsterType.SKELETON:
            StdDraw.picture(picture.Picture("skeleton.gif"), drawX, drawY)
        elif self.type == MonsterType.ORC:
            StdDraw.picture(picture.Picture("orc.gif"), drawX, drawY)
        elif self.type == MonsterType.SLIME:
            StdDraw.picture(picture.Picture("slime.gif"), drawX, drawY)
        elif self.type == MonsterType.BAT:
            StdDraw.picture(picture.Picture("bat.gif"), drawX, drawY)
        
        pass

    #
    # Get the number of hit points the monster has ramaining
    # 
    # return the number of hit points
    def getHitPoints(self):

        return self.hp

    #
    # Get the amount of damage a monster causes
    # 
    # return amount of damage monster causes
    def getDamage(self):

        return self.damage

    #
    # Get the x position of the monster
    # 
    # return x position
    def getX(self):

        return self.x

    #
    # Get the y position of the monster
    # 
    # return y position
    def getY(self):

        return self.y

    #
    # Set the new location of the monster
    # 
    # param x the new x location
    # param y the new y location
    def setLocation(self, x, y):

        self.x = x
        self.y = y
        pass

    #
    # Thread that moves the monster around periodically
    def run(self):
        t1 = threading.Thread(target=draw)
        t2 = threading.Thread(target=draw)

        t1.start()
        time.sleep(self.sleepMs)
        num = random.randint(1,4)
        if num == 1:
            self.x += 1
        elif num == 2:
            self.x -= 1
        elif num == 3:
            self.y += 1
        elif num == 4:
            self.y -= 1
        t2.start()
        
        
        pass
