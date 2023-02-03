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
from random import randint

#
# Class for the MindReader game
#
# To play the game, you only need to call MindReader.playGame
#
class MindReader:

    #
    # Initializer for the MindReader class
    #
    # Inputs: None
    #    
    def __init__(self):
        ''' notes for self.history:
            key: String of past four guesses (ex. 'TTTT' or 'HHTH')
            value: two element list of number of times user guesses heads and tails after key string
                (ex. self.history['HHTH'] = [0,1] means that after the user guesses 'H','H','T', and 'H'
                in that order, they have guessed 'H' zero, and 'T' one times)
        '''
        self.history = {}
        self.pastFourGuesses = []
        self.playerScore = 0
        self.computerScore = 0
        self.userInput = ""
        self.computerPrediction = ""
            
    def updatePastFourGuesses(self):
        if len(self.pastFourGuesses) >= 4:
            self.pastFourGuesses.pop(0)
        self.pastFourGuesses.append(self.userInput)

    def updateHistory(self):
        lastFourString = "".join(self.pastFourGuesses)
        if lastFourString not in self.history:
            self.history[lastFourString] = [1,0] if (self.userInput == "H") else [0,1]
        else:
            currentHistoryTally = self.history[lastFourString]
            currentHistoryTally[0] += 1 if self.userInput == "H" else 0
            currentHistoryTally[1] += 1 if self.userInput == "T" else 0

    def getUserInput(self):
        while self.userInput not in ['h','t','H','T']:
            self.userInput = input("Enter H for heads or T for tails: ")
        if self.userInput.islower():
            self.userInput = self.userInput.upper()

    def getRandomGuess(self):
        value = randint(0, 100)
        if value < 50:
            return "H"
        return "T"

    def getComputerPrediction(self):
        if len(self.pastFourGuesses) < 4:
            self.computerPrediction = self.getRandomGuess()
        else:
            lastFourString = "".join(self.pastFourGuesses)
            if (lastFourString not in self.history) or (self.history[lastFourString][0] == self.history[lastFourString][1]):
                self.computerPrediction = self.getRandomGuess()
            else:
                playerHistoryResults = self.history[lastFourString]
                self.computerPrediction = 'H' if (playerHistoryResults[0] > playerHistoryResults[1]) else 'T'

    def computerGuessedCorrect(self):
        return self.userInput == self.computerPrediction

    def resetGuesses(self):
        self.userInput = ""
        self.computerPrediction = ""

    def playGame(self):
        while (self.playerScore < 20) and (self.computerScore < 20):
            self.getUserInput()
            self.getComputerPrediction()
            print(f"Computer predicted: {self.computerPrediction} Player chose: {self.userInput}")
            if self.computerGuessedCorrect():
                self.computerScore += 1
            else: 
                self.playerScore += 1

            self.updateHistory()
            self.updatePastFourGuesses()
            self.resetGuesses()

            print(f"Computer: {self.computerScore} Player: {self.playerScore}\n")

        if self.playerScore == 20:
            print("You WIN!!!")
        else:
            print("Computer WINS!!!")


if __name__ == "__main__":
    game = MindReader()
    game.playGame()

        