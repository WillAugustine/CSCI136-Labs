from random import randint

class MindReader:

    def __init__(self):
        self.history = {}
        self.pastFourGuesses = []
        self.playerScore = 0
        self.computerScore = 0

    def getUserInput(self):
        userInput = ""
        while userInput not in ['h','t','H','T']:
            userInput = input("Enter H for heads or T for tails: ")
        if userInput.islower():
            userInput = userInput.upper()
        return userInput

    def getRandomGuess(self):
        value = randint(0, 100)
        if value < 50:
            return "H"
        return "T"

    def getComputerPrediction(self):
        if len(self.pastFourGuesses) < 4:
            computerGuess = self.getRandomGuess()
        else:
            if self.pastFourGuesses not in self.history:
                computerGuess = self.getRandomGuess()
        return computerGuess
            

    def getResult(self, userGuess, computerGuess):
        lastFourString = "".join(self.pastFourGuesses)
        if lastFourString not in self.history:
            self.history[lastFourString] = [1,0] if (userGuess == "H") else [0,1]
        else:
            currentGuess = self.history[lastFourString]
            currentGuess[0] += 1 if userGuess == "H" else 0
            currentGuess[1] += 1 if userGuess == "T" else 0
        if len(self.pastFourGuesses) >= 4:
            self.pastFourGuesses.pop(0)
        self.pastFourGuesses.append(userGuess)
        return userGuess == computerGuess

    def playGame(self):
        while (self.playerScore < 20) and (self.computerScore < 20):
            pass

if __name__ == "__main__":
    game = MindReader()

        