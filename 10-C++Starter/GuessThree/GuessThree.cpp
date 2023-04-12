#include <iostream>
#include <random>
#include <string>
#include <time.h>

using namespace std;

bool validInput(string input) {
	if (stoi(input) >= 1 && stoi(input) <= 10) {
		return true;
	}
	return false;
}

int main() {

	int minRandom = 1;
	int maxRandom = 10;
	srand(time(NULL));
	int randomNum = rand() % maxRandom + minRandom;

	for (int i = 0; i < 3; i++) {

		string input = "-1";
		while (!validInput(input)) {
			cout << "Guess a number between 1 and 10: ";
			cin >> input;
		}
		int userGuess = stoi(input);
		if (userGuess == randomNum) {
			cout << "You got it!" << endl;
			i = 3;
		}
		else if (userGuess < randomNum) {
			cout << "Your guess was too low." << endl;
		}
		else {
			cout << "Your guess was too high." << endl;
		}
	}
}