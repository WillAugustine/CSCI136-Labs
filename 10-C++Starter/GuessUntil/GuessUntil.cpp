#include <iostream>
#include <string>
#include <random>
#include <time.h>

using namespace std;

bool validInput(string input) {
	if (stoi(input) >= 1 && stoi(input) <= 100) {
		return true;
	}
	return false;
}

int main() {

	int minRandom = 1;
	int maxRandom = 100;
	srand(time(NULL));
	int randomNum = rand() % maxRandom + minRandom;

	string input = "-1";
	int userGuess = stoi(input);

	while (userGuess != randomNum) {
		input = "-1";

		while (!validInput(input)) {
			cout << "\nGuess a number between 1 and 100: ";
			cin >> input;
		}
		userGuess = stoi(input);

		if (userGuess == randomNum) {
			cout << "You got it!" << endl;
		}
		else if (userGuess < randomNum) {
			cout << "Your guess was too low." << endl;
		}
		else {
			cout << "Your guess was too high." << endl;
		}
	}
}