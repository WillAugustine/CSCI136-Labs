#
# Author: Will Augustine
#
# Description: 
#
import StdDraw
from Tile import Tile
from picture import Picture as pic

class Avatar :

    # Constructor for the avatar class
    #
    # Input parameters x and y are the initial integer positions of the
    #    avatar within the world
    def __init__(self, x, y):
        self.MIN_TORCH = 2.0
        self.MAX_TORCH = 20.0
        self.TORCH_INCREMENT = 0.5
        self.x = x
        self.y = y
        self.torchRadius = 4.0

    # Mutator method to set the avatar to a new location
    #
    # Input parameters are the new integer x and y position
    def setLocation(self, x, y):

        self.x = x
        self.y = y

    # Accessor method
    #
    # Returns the x position of the avatar
    def getX(self):

        return self.x
    
    # Accessor method
    #
    # Returns the y position of the avatar
    def getY(self):

        return self.y
    
    # Accessor method
    #
    # Returns the current radius of the torch
    def getTorchRadius(self):

        return self.torchRadius

    # Make our torch more powerful
    #
    # Increases the radius of the torch
    def increaseTorch(self):

        if self.torchRadius < self.MAX_TORCH:
            self.torchRadius += self.TORCH_INCREMENT
    
    # Make our torch less powerful
    #
    # Decreases the radius of the torch
    def decreaseTorch(self):

        if self.torchRadius > self.MIN_TORCH:
            self.torchRadius -= self.TORCH_INCREMENT

    # Draw the avatar
    #
    # Uses the avatar's current position to place and draw the avatar
    #    on the canvas
    def draw(self):
        SIZE = 16
        x = self.x*SIZE + SIZE/2
        y = self.y*SIZE + SIZE/2
        
        tile = pic('avatar.gif')
        StdDraw.picture(tile, x, y)

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
