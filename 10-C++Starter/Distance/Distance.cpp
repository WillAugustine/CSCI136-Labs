#include <stdio.h>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main(int argc, char* argv[]) {

	if (argc < 5) {
		cout << "Invalid use! Use should be:" << endl;
		cout << "\tDistance.cpp x1 y1 x2 y2" << endl;
	}
	else {
		int x1 = stoi(argv[1]);
		int y1 = stoi(argv[2]);
		int x2 = stoi(argv[3]);
		int y2 = stoi(argv[4]);

		float distance = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
		cout << "The distance between ";
		cout << "(" << x1 << ", " << y1 << ") ";
		cout << "and ";
		cout << "(" << x2 << ", " << y2 << ") ";
		cout << "is ";
		cout << distance << endl;
	}

}