#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <fstream>
#include <math.h>
#include <time.h>
#include <sstream>
#include <array>

using namespace std;

class GreedyPath {

private:
	int numOfPoints = 0;
	float totalDistance = 0.0;
	int runTime = 0;
	float* xPoints;
	float* yPoints;
	bool* visited;
	clock_t startTime = clock();

public:
	string filename;

	void readFile() {
		string line;
		ifstream fileReader(filename);
		bool firstLineRead = false;
		int counter = 0;
		getline(fileReader, line);
		numOfPoints = stoi(line);
		xPoints = new float[numOfPoints];
		yPoints = new float[numOfPoints];
		visited = new bool[numOfPoints];
		while (getline(fileReader, line)) {
			stringstream ss(line);
			float x, y;
			ss >> x >> y;
			xPoints[counter] = x;
			yPoints[counter] = y;
			visited[counter] = false;
			counter++;
		}
		fileReader.close();
	}

	void printOutput() {
		runTime = (clock() - startTime) / CLOCKS_PER_SEC;
		cout << "Number of Points - " << numOfPoints << endl;
		cout << "Total Distance = " << totalDistance << endl;
		cout << "Elapsed Time (sec) - " << runTime << endl;
	}

	void calculateDistance() {
		int currIndex = 0;
		visited[currIndex] = true;
		for (int i = 0; i < numOfPoints - 1; i++) {
			float minDistance = INFINITY;
			int next;
			for (int j = 0; j < numOfPoints; j++) {
				if (!visited[j]) {
					float xDelta = xPoints[j] - xPoints[currIndex];
					float yDelta = yPoints[j] - yPoints[currIndex];
					float currDistance = xDelta * xDelta + yDelta * yDelta;
					if (currDistance < minDistance) {
						minDistance = currDistance;
						next = j;
					}
				}
			}
			totalDistance += sqrt(minDistance);
			currIndex = next;
			visited[currIndex] = true;
		}
		float xDelta = xPoints[0] - xPoints[currIndex];
		float yDelta = yPoints[0] - yPoints[currIndex];
		totalDistance += sqrt(xDelta * xDelta + yDelta * yDelta);
	}

};

int main(int argc, char* argv[]) {

	GreedyPath path;

	if (argc != 2) {
		cout << "Invalid use of file! Please run the program like:" << endl;
		cout << "\tGreedyPath.exe <input file name>" << endl;
		path.filename = "points7.txt";
		
	}
	else {
		path.filename = argv[1];
	}

	path.readFile();
	path.calculateDistance();
	path.printOutput();
	
	
}