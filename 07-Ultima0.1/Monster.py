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
    INVALID = None
    SKELETON = {'filename': 'skeleton.gif'} # For code 'SK'
    ORC = {'filename': 'orc.gif'} # For code 'OR'
    SLIME = {'filename': 'slime.gif'} # For code 'SL'
    BAT = {'filename': 'bat.gif'} # For code 'BA'

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

        self.world = world
        if code == 'SK':
            self.attributes = MonsterType.SKELETON.value
        elif code == 'OR':
            self.attributes = MonsterType.ORC.value
        elif code == 'SL':
            self.attributes = MonsterType.SLIME.value
        elif code == 'BA':
            self.attributes = MonsterType.BAT.value
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.sleepTime = sleepMs
        self.isDead = False

    # The avatar has attacked a monster!
    #
    # param points	- number of hit points to be subtracted from monster
    def incurDamage(self, points):

        self.hp -= points
        if self.hp <= 0:
            self.isDead = True

    #
    # Draw this monster at its current location
    def draw(self):
        if not self.isDead:
            image = picture.Picture(self.attributes['filename'])
            StdDraw.picture(image, self.x, self.y)
        

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
        if x > self.x:
            direction = 'right'
        elif x < self.x:
            direction = 'left'
        elif y > self.y:
            direction = 'up'
        elif y < self.y:
            direction = 'down'
        if self.monsterCanMove(direction):
            self.x = x
            self.y = y

    def monsterCanMove(self, direction):
        if (direction ==  'up'): # If specified direction is up
            return True if self.world[self.y + 1][self.x].isPassable() else False
        if (direction == 'down'): # If specified direction is down   
            return True if self.world[self.y - 1][self.x].isPassable() else False
        if (direction == 'left'): # If specified direction is left
            return True if self.world[self.y][self.x - 1].isPassable() else False
        if (direction == 'right'): # If specified direction is right
            return True if self.world[self.y][self.x + 1].isPassable() else False

    #
    # Description: Used to move the avatar in the specified direction
    # 
    # Inputs:
    #   string direction: Either 'up', 'down', 'right', or 'left'
    # 
    # Outputs:
    #   None
    #
    def moveMonster(self, direction):
        if (direction ==  'up'): # If specified direction is up
            self.setLocation(self.x, self.y + 1)
        if (direction == 'down'): # If specified direction is down       
            self.setLocation(self.x, self.y - 1)
        if (direction == 'left'): # If specified direction is left
            self.setLocation(self.x - 1, self.y)
        if (direction == 'right'): # If specified direction is right
            self.setLocation(self.x + 1, self.y)


    #
    # Thread that moves the monster around periodically
    def run(self):
        directions = ['up', 'down', 'left', 'right']
        directionToMove = random.choice(directions)
        while not self.monsterCanMove(directionToMove):
            directionToMove = random.choice(directions)
        self.moveMonster(directionToMove)