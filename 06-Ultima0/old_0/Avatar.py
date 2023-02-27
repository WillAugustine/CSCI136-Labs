#
# Author: 
#
# Description: 
#
import StdDraw
from Tile import Tile
import picture

class Avatar :

    # Constructor for the avatar class
    #
    # Input parameters x and y are the initial integer positions of the
    #    avatar within the world
    def __init__(self, x, y):

        ##### YOUR CODE HERE #####
        pass

    # Mutator method to set the avatar to a new location
    #
    # Input parameters are the new integer x and y position
    def setLocation(self, x, y):

        ##### YOUR CODE HERE #####
        pass

    # Accessor method
    #
    # Returns the x position of the avatar
    def getX(self):

        #####YOUR CODE HERE #####
        return 0
    
    # Accessor method
    #
    # Returns the y position of the avatar
    def getY(self):

        ##### YOUR CODE HERE #####
        return 0
    
    # Accessor method
    #
    # Returns the current radius of the torch
    def getTorchRadius(self):

        ##### YOUR CODE HERE #####
        return 0

    # Make our torch more powerful
    #
    # Increases the radius of the torch
    def increaseTorch(self):

        ##### YOUR CODE HERE #####
        pass
    
    # Make our torch less powerful
    #
    # Decreases the radius of the torch
    def decreaseTorch(self):

        #####YOUR CODE HERE #####
        pass

    # Draw the avatar
    #
    # Uses the avatar's current position to place and draw the avatar
    #    on the canvas
    def draw(self):

        ##### YOUR CODE HERE #####
        pass

# Main code to test the avatar class    
if __name__ == "__main__":
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
