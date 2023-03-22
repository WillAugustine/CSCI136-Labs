#
# Author: Will Augustine
#
# Description: Draws and modifies the world for the Ultima game
#

# Imports
from Tile import Tile # Imports Tile class from Tile.py
from Avatar import Avatar # Imports Avatar class from Avatar.py
import sys # Imports sys for reading in command line arguments
import StdDraw # Imports StdDraw for drawing world
from Monster import Monster # Imports Monster class from Monster.py
from threading import Thread, Lock # Imports used for monster and avatar threading

class World:

    #
    # Description: Constructor for the World class
    # 
    # Inputs:
    #   string filename: the file you want to read in
    #
    # Outputs:
    #   N/A
    #
    def __init__(self, filename):
        fileReader = open(filename, 'r') # Variable for all input file information
        fileContents = fileReader.read().splitlines() # Array of strings from input file
        
        self.width = int(fileContents[0].split()[0]) # Get the inputted width
        self.height = int(fileContents[0].split()[1]) # Get the inputted height
        del fileContents[0] # Deletes the line we just read

        # Converts first four elements on the avatar's line to int and stores them in an array
        avatarVals = [int(x) for x in fileContents[0].split()[:4]]
        avatarVals.append(float(fileContents[0].split()[4])) # Adds the starting torch radius to the avatar's values
        self.avatarX = avatarVals[0] # Defines variable to store avatar's current x
        self.avatarY = avatarVals[1] # Defines variable to store avatar's current y

        # Variable for object of avatar class (want the same avatar througout the game)
        self.avatar = Avatar(avatarVals[0], avatarVals[1], avatarVals[2], avatarVals[3], avatarVals[4]) 
        del fileContents[0] # Deletes the line we just read

        self.world = [] # Variable for world of Tile class object
        # Loop to extract world character, create Tile object from character, then add Tile object
        #   to the self.world variable in the correct spot
        for lineNum in range(self.height): # For each row
            lineContents = fileContents[lineNum].split()
            temp = []
            for colNum in range(self.width): # For each character in the row
                temp.append(Tile(lineContents[colNum])) # Add Tile object to self.world
            self.world.append(temp)
        self.world = list(reversed(self.world)) # Reverses the world
        del fileContents[:self.height] # Deletes the lines we just read

        self.monsters = [] # Variable for the monsters still in the game
        self.monsterThreads = [] # Variable for the monter's threads still in the game
        for monster in [x.split() for x in fileContents]: # For each monster's specifications in the input file
            monsterVals = [int(x) for x in monster[1:]] # Create an array of the monster variables
            monsterVals.insert(0, monster[0]) # Add the monster's code to the monster variable array

            # Creates an object of the monster class (want the same monsters all game)
            monster = Monster(self, monsterVals[0], monsterVals[1], monsterVals[2], monsterVals[3], monsterVals[4], monsterVals[5])
            self.monsters.append(monster) # Add new monster to monsters in the game array
            thread = Thread(target=monster.run) # Create a thread from the new monster
            self.monsterThreads.append(thread) # Add the thread to the array of monster threads
        self.lock = Lock() # Variable for threading lock
        self.size = 16 # Variable for the size of a tile

        # Set up a StdDraw canvas on which to draw the tiles
        StdDraw.setCanvasSize(self.width * self.size, self.height * self.size)
        StdDraw.setXscale(0.0, self.width * self.size)
        StdDraw.setYscale(0.0, self.height * self.size)

        # Sets pen color and size for displaying monster damage 
        StdDraw.setFontSize(12)
        StdDraw.setPenColor(StdDraw.RED)

        # Start the monster's threads
        for thread in self.monsterThreads:
            thread.start()

    #
    # Description: Eliminated an inputted monster from the game
    # 
    # Inputs:
    #   Monster monster: The monster you wish to remove from the game
    # 
    # Outputs:
    #   None
    #
    def removeMonster(self, monster):
        index = self.monsters.index(monster) # Gets the index of the inputted monster
        del self.monsters[index] # Removes monster from monsters index
        del self.monsterThreads[index] # Removes monster from monster threads index

    #
    # Description: Used to determine if the avatar can move in the specified direction
    # 
    # Inputs:
    #   int x: Desired x position for the avatar to move to
    #   int y: Desired y position for the avatar to move to
    # 
    # Outputs:
    #   True: If the avatar CAN move in the specified direction    
    #   False: If the avatar CANNOT move in the specified direction
    #
    def canMoveAvatar(self, x, y):
        '''
            If the desired x position is out of bounds or
            if the desired y position if out of bounds or
            if the desired tile is not passable
        '''
        if x not in range(self.width) or \
            y not in range(self.height) or \
            not self.world[y][x].isPassable():
            return False # Return False
        for monster in self.monsters: # For each monster still alive
            if ((monster.getX() == x) and (monster.getY() == y)): # If the desired location has a monster there
                monster.incurDamage(self.avatar.getDamage()) # Attack the monster
                if monster.getHitPoints() <= 0: # If the monster's hit points are less than or equal to 0
                    self.removeMonster(monster) # Remove the monster from the game
                else: # If the monster is still alive
                    return False # Return False (cannot move ontop of monster)
        return True # Return True


    #
    # Description: Used to move the avatar in the specified direction
    # 
    # Inputs:
    #   string direction: Either 'up', 'down', 'right', or 'left'
    # 
    # Outputs:
    #   None
    #
    def avatarMove(self, direction):
        newX = self.avatar.getX() # Sets newX to current x
        newY = self.avatar.getY() # Sets newY to current y
        if (direction ==  'up'): # If specified direction is up
            newY += 1 # Increase newY
        if (direction == 'down'): # If specified direction is down       
            newY -= 1 # Decrease newY
        if (direction == 'left'): # If specified direction is left
            newX -= 1 # Decrease newX
        if (direction == 'right'): # If specified direction is right
            newX += 1 # Increase newX
        if self.canMoveAvatar(newX, newY): # If the avatar can move in the desired direction
            self.avatar.setLocation(newX, newY) # Move the avatar
            self.avatar.incurDamage(self.world[newY][newX].getDamage()) # Take damage if moved onto lava
        self.avatarX = self.avatar.getX() # Updates self.avatarX with current avatar x
        self.avatarY = self.avatar.getY() # Updates self.avatarY with current avatar y
        
    #
    # Description: Handles a key pressed and either moves the avatar or modifies torch brightness
    # 
    # Inputs:
    #   char ch: The key that was pressed
    # 
    # Outputs:
    #   None
    #
    def handleKey(self, ch):
        ch = ch.lower() # Converts passed character to lowercase (incase caps lock is on)

        self.lock.acquire() # Aquires a lock for threading

        if (ch == 'w'): # If the player clicked 'w'
            self.avatarMove('up') # If the avatar can move up, move the avatar up

        elif (ch == 's'): # If the player clicked 's'
            self.avatarMove('down') # If the avatar can move down, move the avatar down

        elif (ch == 'a'): # If the player clicked 'a'
            self.avatarMove('left') # If the avatar can move left, move the avatar left

        elif (ch == 'd'): # If the player clicked 'd'
            self.avatarMove('right') # If the avatar can move right, move the avatar right

        elif (ch == '+'): # If the player clicked '+'
            self.avatar.increaseTorch() # Increase the torch radius

        elif (ch == '-'): # If the player clicked '-'
            self.avatar.decreaseTorch() # Decrease the torch radius
        
        self.lock.release() # Releases the thread lock

    #
    # Description: Determines if the avatar is still alive
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   True: If the avatar's hit points are greater than 0
    #   False: If the avatar's hit points are less than or equal to 0
    #
    def avatarAlive(self):
        return False if self.avatar.getHitPoints() <= 0 else True
    
    #
    # Description: Determines if a monster can move to a desired location
    #   by seeing if there would be a collision with another monster
    # 
    # Inputs:
    #   int x: Desired x position for the monster to move to
    #   int y: Desired y position for the monster to move to
    # 
    # Outputs:
    #   True: If a monster CAN move to the desired location
    #   False: If a monster CANNOT move to the desired location
    #
    def monsterCanMove(self, x, y):
        for monster in self.monsters: # For each monster still alive
            '''
                If there is a monster at the desired location
            '''
            if monster.getX() == x and \
            monster.getY() == y:
                return False # Return False (monster CANNOT move there)
        return True # Return True (monster CAN move there)

    #
    # Description: Moves a monster to inputted x and y if the monster is able to move there
    # 
    # Inputs:
    #   int x: Desired x position for the monster to move to
    #   int y: Desired y position for the monster to move to
    #   Monster monster: The monster you want to move
    # 
    # Outputs:
    #   None
    #
    def monsterMove(self, x, y, monster):
        self.lock.acquire() # Aquires a lock for threading
        '''
            If x is within bounds and
            y is within bounds and
            the desired tile is passable
        '''
        if x in range(self.width) and \
        y in range(self.height) and \
        self.world[y][x].isPassable():
            if self.monsterCanMove(x, y): # If the monster can move to the desired location
                if self.avatar.getX() == x and self.avatar.getY() == y: # If the avatar is at the desired location
                    self.avatar.incurDamage(monster.getDamage()) # Attack the avatar
                else: # If the avatar is not at the desired location
                    monster.setLocation(x, y) # Move the monster
                    monster.incurDamage(self.world[y][x].getDamage()) # Take damage is moved onto lava
                    if monster.getHitPoints() <= 0: # If the monster has no more hit points
                        self.removeMonster(monster) # Remove the monster from the game
        self.lock.release() # Releases the thread lock

    #
    # Description: Gets the number of monsters left in the game
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   The number of monsters left in the game
    #
    def getNumMonsters(self):
        return len(self.monsters) # Returns the length of the monster array

    #
    # Description: Draws the world
    # 
    # Inputs:
    #   None
    # 
    # Outputs:
    #   None
    #
    def draw(self):
        self.setLit(False) # Sets all tiles to unlit
        self.light(self.avatarX, self.avatarY, self.avatar.getTorchRadius()) # Lights tiles around avatar based on torch radius
        for y in range(self.height): # Traverse through the column index
            for x in range(self.width): # For each index (row) in each column
                self.world[y][x].draw(x, y) # Draw the current tile
        for monster in self.monsters:
            monster.draw() # Draws the monsters on top of the tiles
        self.avatar.draw() # Draw the avatar on top of the tiles
    
    #
    # Description: Calls lightDFS to light up tiles based on opaque values and torch radius
    # 
    # Inputs:
    #   int x: Avatar's x position
    #   int y: Avatar's y position
    #   float r: radius of the Avatar's torch 
    #
    # Outputs:
    #   Number of tiles lit
    #
    def light(self, x, y, r):
        return self.lightDFS(x, y, x, y, r) # Calls lightDFS to light surrounding area and returns number of tiles lit

    #
    # Description: A recursive function to light up nearby tiles based on torch strength
    # 
    # Inputs:
    #   int x: Avatar's x position
    #   int y: Avatar's y position
    #   int currX: The current x position being looked at
    #   int currY: The current y position being looked at
    #   float r: radius of the Avatar's torch 
    #
    # Outputs:
    #   Number of tiles lit
    #
    def lightDFS(self, x, y, currentX, currentY, r):
        dist = ((currentX - x)**2 + (currentY - y)**2)**0.5 # Calculates the distance from avatar to current position
        
        litTiles = 0 # Set litTiles equal to 0 since no tiles are lit yet
        '''
            if currentX is within bounds and
            currentY is within bounds and
            the current tile is not lit and
            distance from tile to avatar is less than torch radius
        '''
        if currentX in range(self.width) and \
            currentY in range(self.height) and \
            not self.world[currentY][currentX].getLit() and \
            dist < r:
            
            if self.world[currentY][currentX].isOpaque(): # If a block is opaque (you cannot see through it)
                self.world[currentY][currentX].setLit(True) # Set the tile as lit
                return 1 # Do not light any more tiles after opaque tile
            self.world[currentY][currentX].setLit(True) # Set the tile as lit
            litTiles += 1 # Increment number of tiles lit
        else: # Base case
            return 0 # Return 0 since no tiles were lit this go around
        litTiles += self.lightDFS(x, y, currentX-1, currentY, r) # Light the tile to the left
        litTiles += self.lightDFS(x, y, currentX, currentY-1, r) # Light the tile above
        litTiles += self.lightDFS(x, y, currentX+1, currentY, r) # Light the tile to the right
        litTiles += self.lightDFS(x, y, currentX, currentY+1, r) # Light the tile below
        return litTiles # Return the number of tiles lit

    #
    # Description: Sets all tiles in the world to a specified lit value
    # 
    # Inputs:
    #   boolean value: The desired lit value for all tiles in the world
    #
    # Outputs:
    #   None
    #
    def setLit(self, value):

        for row in self.world: # For each row in the world 
            for tile in row: # For each tile in the current row
                tile.setLit(value) # Set the lit value equal to the inputted value
    
# Main code to test the world class
if __name__ == "__main__":
    world0 = World(sys.argv[1])
    world0.draw()
    StdDraw.show()
