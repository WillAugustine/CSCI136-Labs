# 
# Author: Will Augustine
# 
# Description: Contains the Monster class which is responsible for manipulating monsters
#   within the world
#

from enum import Enum # Import for monster attributes enumeration class
import time # Import for waiting between monster movements
import StdDraw # Import for drawing monsters
import picture # Import for creating picture object of monster
import random # Import for randomly selecting direction to move monster
from Tile import Tile # Import for getting size of tiles

# Enumeration class for dealing with different monster types
class MonsterType(Enum):
    INVALID = None
    SKELETON = {'filename': 'skeleton.gif'} # For code 'SK'
    ORC = {'filename': 'orc.gif'} # For code 'OR'
    SLIME = {'filename': 'slime.gif'} # For code 'SL'
    BAT = {'filename': 'bat.gif'} # For code 'BA'

class Monster:

    #
    # Description: Constructor for the Monster class
    # 
    # Inputs:
    #   World world: The world the monster moves about in
    #   string code: The string code that distinguishes types of monsters
    #   int x: The x position of the monster
    #   int y: The y position of the monster
    #   int hp: Hit points - damage sustained by the monster
    #   int damage: Damage the monster causes
    #   int sleepMs: Delay between time monster moves
    # 
    # Outputs:
    #   N/A
    #
    def __init__(self, world, code, x, y, hp, damage, sleepMs):

        self.world = world # Variable for the world object
        if code == 'SK': # If the monster is a skeleton
            self.attributes = MonsterType.SKELETON.value # Get attributes defined by MonsterType enumeration
        elif code == 'OR': # If the monster is a orc
            self.attributes = MonsterType.ORC.value # Get attributes defined by MonsterType enumeration
        elif code == 'SL': # If the monster is a slime
            self.attributes = MonsterType.SLIME.value # Get attributes defined by MonsterType enumeration
        elif code == 'BA': # If the monster is a bat
            self.attributes = MonsterType.BAT.value # Get attributes defined by MonsterType enumeration
        self.x = x # Variable for monster's current x
        self.y = y # Variable for monster's current y
        self.nextX = x # Variable for monster's desired x
        self.nextY = y # Variable for monster's desired y
        self.hp = hp # Variable for monster's health points
        self.damage = damage # Variable for the amount of damage the monster deals
        self.sleepTime = sleepMs # Variable for the time interval between movements
        self.damageTimer = 0 # Variable for cycles before damage message goes away

    #
    # Description: Deals a specified amount of damage to the monster
    # 
    # Inputs:
    #   int points: The damage dealt to the monster
    # 
    # Outputs:
    #   None
    #
    def incurDamage(self, points):
        if points > 0:
            self.damageTimer = 3 # Reset the number of cycles until the damage display goes away
        self.hp -= points # Reduce the monster's health points

    #
    # Description: Converts an x value into it's pixel value based on tile size
    # 
    # Inputs:
    #   int x: The x value to be converted
    # 
    # Outputs:
    #   The pixel x value
    #
    def getPixelX(self, x):
        return x * Tile.SIZE + (Tile.SIZE / 2)
    
    #
    # Description: Converts a y value into it's pixel value based on tile size
    # 
    # Inputs:
    #   int y: The y value to be converted
    # 
    # Outputs:
    #   The pixel y value
    #
    def getPixelY(self, y):
        return y * Tile.SIZE + (Tile.SIZE / 2)

    #
    # Description: Draws a monster if the tile the monster is on is lit and 
    #   display the amount of damage taken for three cycles
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   None
    #
    def draw(self):
        if self.world.world[self.y][self.x].getLit(): # If the tile the monster is on is lit
            x = self.getPixelX(self.x) # Convert x into pixel x (for drawing)
            y = self.getPixelY(self.y) # Convert y into pixel y (for drawing)
            image = picture.Picture(self.attributes['filename']) # Creates picture object to be passed into StdDraw.picture
            StdDraw.picture(image, x, y) # Draws the picure
            if self.damageTimer > 0: # If the monster has taken damage less than three cycles ago
                StdDraw.text(x, y, str(self.hp)) # Display the amount of damage taken
        

    #
    # Description: Gets the number of health points the monster has left
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   The health points the monster has left
    #
    def getHitPoints(self):

        return self.hp

    #
    # Description: Gets the amount of damage the monster deals
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   The amount of damage the monster deals
    #
    def getDamage(self):

        return self.damage

    #
    # Description: Gets the monster's current x position
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   The monster's current x position
    #
    def getX(self):

        return self.x

    #
    # Description: Gets the monster's current y position
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   The monster's current y position
    #
    def getY(self):

        return self.y

    #
    # Description: Sets the monster's position based on inputted x and y points
    # 
    # Inputs:
    #   
    # 
    # Outputs:
    #   The monster's current x position
    #
    def setLocation(self, x, y):
        self.x = x
        self.y = y

    #
    # Description: Used to move the avatar in the specified direction
    # 
    # Inputs:
    #   string direction: Either 'up', 'down', 'right', or 'left'
    # 
    # Outputs:
    #   None
    #
    def getNextMonsterPosition(self, direction):
        self.nextX = self.x # Defaults self.nextX to current monster's x position
        self.nextY = self.y # Defaults self.nextY to current monster's y position
        if (direction ==  'up'): # If specified direction is up
            self.nextY += 1 # Increase self.nextY by 1
        if (direction == 'down'): # If specified direction is down       
            self.nextY =- 1 # Decrease self.nextY by 1
        if (direction == 'left'): # If specified direction is left
            self.nextX -= 1 # Decrease self.nextX by 1
        if (direction == 'right'): # If specified direction is right
            self.nextX += 1 # Increase self.nextX by 1


    #
    # Description: Used to move a monster randomly and then have it sleep
    #   for a duration specified in the input file
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   None
    #
    def run(self):
        while self.hp > 0: # While a monster is still alive
            directions = ['up', 'down', 'left', 'right'] # Directions a monster could move
            self.getNextMonsterPosition(random.choice(directions)) # Get the x and y if the monster were to move in random direction
            while not self.world.monsterCanMove(self.nextX, self.nextY): # While the monster cannot move in the selected direction
                self.getNextMonsterPosition(random.choice(directions)) # Select another direction
            self.world.monsterMove(self.nextX, self.nextY, self) # Move the monster
            self.damageTimer -= 1 # Decrement damageTimer (OK if below 0 since only evaluating if greater than 0 - line 113)
            time.sleep(self.sleepTime / 1000) # Have the monster sleep for a specified time from the input file
