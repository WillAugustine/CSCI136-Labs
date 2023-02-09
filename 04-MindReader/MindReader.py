# 
#   Author: Will Augustine
#       Computer Science Senior at Montana Technological University 
#
#   Description: You battle the computer by guessing heads (H) or tails (T)
#       and the computer will use your previous guesses to predict what you will guess.
#       This lab demonstrates the predictability and unknowing patterns of humans.
#
#   Example use:
#       MindReader.py takes in no command line arguments, so you can execute it with:
#       "python MindReader.py"
#

# Imports
from random import randint # Used to get a random integer

#
# Class for the MindReader game
#
# To play the game, you only need to call MindReader.playGame
#
class MindReader:

    #
    # Initializer for the MindReader class
    #
    # Inputs: int maxScore - the maximum score you will play until
    #    
    def __init__(self, maxScore):
        ''' notes for self.history:
            key: String of past four guesses (ex. 'TTTT' or 'HHTH')
            value: two element list of number of times user guesses heads and tails after key string
                (ex. self.history['HHTH'] = [0,1] means that after the user guesses 'H','H','T', and 'H'
                in that order, they have guessed 'H' zero, and 'T' one times)
        '''
        self.history = {}
        # Stores previous four guesses in array of guesses (ex. ['H', 'T', 'H', 'H'])
        self.pastFourGuesses = []
        self.playerScore = 0 # Stores the player's score
        self.computerScore = 0 # Stores the computer's score
        self.userInput = "" # Stores the player's input
        self.computerPrediction = "" # Stores the computer's prediction
        self.maxScore = maxScore # Stores the maximum score possible

    #
    # Updates the self.pastFourGuesses variable using self.userInput
    # 
    # Input: None
    #      
    def updatePastFourGuesses(self):
        if len(self.pastFourGuesses) >= 4: # If the length is four or more
            self.pastFourGuesses.pop(0) # Remove the first element in self.pastFourGuesses
        self.pastFourGuesses.append(self.userInput) # Add user input to the end of self.pastFourGuesses

    #
    # Updates the self.history variable using self.userInput and self.pastFourGuesses
    # 
    # Input: None
    #   
    def updateHistory(self):
        if len(self.pastFourGuesses) < 4:
            return
        lastFourString = "".join(self.pastFourGuesses) # Turns array of self.pastFourGuesses into combined string
        if lastFourString not in self.history: # If the last four guesses have not been guessed before
            self.history[lastFourString] = [1,0] if (self.userInput == "H") else [0,1] # Add it to the self.history dictionary
        else: # If the last four gueses have been guesses before
            currentHistoryTally = self.history[lastFourString] # Get the array of guesses
            currentHistoryTally[0] += 1 if self.userInput == "H" else 0 # Add one to heads history if user input is 'H'
            currentHistoryTally[1] += 1 if self.userInput == "T" else 0 # Add one to tails history if user input is 'T'
            self.history[lastFourString] = currentHistoryTally # Update self.history

    #
    # Gets the user input
    #
    # Input: None
    #
    def getUserInput(self):
        while self.userInput not in ['h','t','H','T']: # If the input is not 'h', 't', 'H', or 'T'
            self.userInput = input("Please enter H for heads or T for tails: ") # Ask for the user's input and update self.userInput
        if self.userInput.islower(): # If the user's input was lowercase
            self.userInput = self.userInput.upper() # Make the user's input uppercase

    #
    # Gets a random guess for the computer
    #
    # Input: None
    #
    # Output: String
    #
    def getRandomGuess(self):
        value = randint(0, 100) # Set value equal to a random number from 0-99
        if value < 50: # If value is less than 50
            return "H" # Computer's guess is heads
        return "T" # Otherwise, computer's guess is tails

    #
    # Gets the computer's prediction using getRandomGuess or self.history
    #
    # Input: None
    #
    def getComputerPrediction(self):
        if len(self.pastFourGuesses) < 4: # If there have been less than four previous guesses
            self.computerPrediction = self.getRandomGuess() # Use getRandomGuess to get computer's prediction
        else:
            lastFourString = "".join(self.pastFourGuesses) # Turns array of self.pastFourGuesses into combined string
            ''' If the last four guesses have not been guesses before OR
                If the quantity of the next guess after the last four guesses are equal
            '''
            if (lastFourString not in self.history) or (self.history[lastFourString][0] == self.history[lastFourString][1]):
                self.computerPrediction = self.getRandomGuess() # Use getRandomGuess to get computer's prediction
            else:
                playerHistoryResults = self.history[lastFourString] # Get the array of quantities of guesses after last four guesses
                ''' If the first element in the quantity of the next guess after the last four guesses is greater than
                    the second element, 'H' is most likely to be guessed. Othersise, 'T' is most likely to be guessed
                '''
                self.computerPrediction = 'H' if (playerHistoryResults[0] > playerHistoryResults[1]) else 'T'

    #
    # Determines if the computer guesses correctly
    #
    # Input: None
    #
    # Output: Boolean
    #
    def computerGuessedCorrect(self):
        return self.userInput == self.computerPrediction # Returns if user input is equal to computer prediction

    # 
    # Resets the user's input and the computer's prediction variables
    #
    # Input: None
    #
    def resetGuesses(self):
        self.userInput = "" # Reset user input
        self.computerPrediction = "" # Reset computer prediction

    # 
    # Prints the instructions on how to play the game followed by a new line
    #
    # Input: None
    #
    def printInstructions(self):
        print("(Instructions for playing...)\n")
        
    #
    # Plays the MindReader game until one score reaches 20
    #
    # Input: None
    #
    def playGame(self):
        self.printInstructions() # Prints the instructions on how to play
        while (self.playerScore < self.maxScore) and (self.computerScore < self.maxScore): # While both scores are less than 20
            print("Your Turn.") # Prints that it is your turn
            self.getComputerPrediction() # Gets the computer prediction
            self.getUserInput() # Gets the user input
            print(f"The computer predicted {self.computerPrediction} and the player chose {self.userInput}.") # Prints what input/prediction was
            if self.computerGuessedCorrect(): # If computer guesses correctly
                self.computerScore += 1 # Increase computer's score by 1
                print("One point for the computer!") # Prints that the computer scored a point
            else: # If the computer guessed incorrectly
                self.playerScore += 1 # Increase player's score by 1
                print("One point for the player.") # Prints that the player scored a point
            self.updateHistory() # Updates self.history
            self.updatePastFourGuesses() # Updates self.pastFourGuesses
            self.resetGuesses() # Resets user input and computer prediction variables

            print(f"Computer: {self.computerScore} , Player: {self.playerScore}\n") # Prints updated scores

        if self.playerScore == self.maxScore: # After one score reaches max score, if that score is the player's score
            print("You WIN!!!") # Print that the player wins
        else: # If the score that hit max score was the computer's score
            print("Computer WINS!!!") # Print that the computer wins


if __name__ == "__main__": # If the file was executed from the command line
    playUntilScore = 25 # Sets the maximum score equal to 25
    game = MindReader(playUntilScore) # Creates object of the MindReader class
    game.playGame() # Calls playGame in the MindReader class

        