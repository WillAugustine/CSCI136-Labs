#
# Author: Will Augustine
#
# Description: Contains the Avatar class where you can move avatar and modify torch radius
#

# Imports
import StdDraw # Import StdDraw to draw avatar
from Tile import Tile # Import Tile class from Tile.py
from picture import Picture as pic # Import Picture class from picture.py as variable 'pic'

class Avatar :

    #
    # Description: Constructor for the Avatar class
    # 
    # Inputs:
    #   int x: Avatar's starting x position
    #   int y: Avatar's starting y position
    #   int hp: The starting hp for the avatar
    #   int damage: The amount of damage the avatar can deal
    #   double torch: The starting torch radius for the avatar
    #
    # Outputs:
    #   N/A
    #
    def __init__(self, x, y, hp, damage, torch):
        self.MIN_TORCH = 2.0 # Defines minimum torch radius
        self.MAX_TORCH = 20.0 # Defines maximum torch radius
        self.TORCH_INCREMENT = 0.5 # Defined torch increment value
        self.x = x # Variable for avatar x position
        self.y = y # Variable for avatar y position
        self.torchRadius = torch # Variable for torch radius
        self.hp = hp # Variable for health points (hp)
        self.damage = damage # Variable for damage the avatar can deal

    #
    # Description: Used to set the location of the avatar
    # 
    # Inputs:
    #   int x: Desired avatar's x position
    #   int y: Desired avatar's y position
    #
    # Outputs:
    #   None
    #
    def setLocation(self, x, y):
        self.x = x # Update x position with inputted value
        self.y = y # Update y position with inputted value

    #
    # Description: Accessor method for the avatar's x position
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   The avatar's x position
    #
    def getX(self):
        return self.x # Returns the avatar's current x position
    
    #
    # Description: Accessor method for the avatar's y position
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   The avatar's y position
    #
    def getY(self):
        return self.y # Returns the avatar's current y position
    
    #
    # Description: Accessor method for the torch radius
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   The torch's current radius
    #
    def getTorchRadius(self):
        return self.torchRadius # Returns the torch radius

    #
    # Description: Used to increase the torch radius
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   None
    #
    def increaseTorch(self):
        if self.torchRadius < self.MAX_TORCH: # If the torch radius is less than the max radius
            self.torchRadius += self.TORCH_INCREMENT # Increment the torch radius by increment value
    
    #
    # Description: Used to decrease the torch radius
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   None
    #
    def decreaseTorch(self):

        if self.torchRadius > self.MIN_TORCH: # If the torch radius is greater than the min radius
            self.torchRadius -= self.TORCH_INCREMENT # Decrement the torch radius by increment value

    #
    # Description: Used to draw the avatar based on current position
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   None
    #
    def draw(self):
        SIZE = 16 # Variable for tile size (in pixels)
        x = self.x*SIZE + SIZE/2 # Calculates pixel x
        y = self.y*SIZE + SIZE/2 # Calculates pixel y
        
        tile = pic('avatar.gif') # Create picture object from avatar image
        StdDraw.picture(tile, x, y) # Draws the avatar

    #
    # Description: Used to access the avatar's health points
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   The health points the avatar has
    #
    def getHitPoints(self):
        return self.hp
    
    #
    # Description: Used to decrease the avatar's hp by damage incurred
    # 
    # Inputs:
    #   int damage: The amount of damage the avatar took
    #
    # Outputs:
    #   None
    #
    def incurDamage(self, damage):
        self.hp -= damage

    #
    # Description: Used to access the amount of damage the avatar can deal
    # 
    # Inputs:
    #   None
    #
    # Outputs:
    #   The amount of damage the avatar deals
    #
    def incurDamage(self):
        return self.damage
    
# Main code to test the avatar class    
if __name__ == "__main__":
    WIDTH = 11
    HEIGHT = 11
    SIZE = 16
    StdDraw.setCanvasSize(WIDTH * SIZE, HEIGHT * SIZE)
    StdDraw.setXscale(0.0, WIDTH * SIZE)
    StdDraw.setYscale(0.0, HEIGHT * SIZE)
    # Create an avatar at 5,5
    avatar = Avatar(5, 5)
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Change the avatar's position
    avatar.setLocation(1, 4)
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Increase the torch radius
    avatar.increaseTorch()
    print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    # Decrease the torch radius 6 times to make sure it doesn't go below 2.0
    for i in range(0, 6):
        avatar.decreaseTorch()
        print("%d %d %.1f" %(avatar.getX(), avatar.getY(), avatar.getTorchRadius()))
    avatar.setLocation(5,5)
    avatar.draw()
    StdDraw.show(5000)
