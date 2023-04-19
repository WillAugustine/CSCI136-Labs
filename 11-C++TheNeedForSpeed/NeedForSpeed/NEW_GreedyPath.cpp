#include <iostream>
#include <fstream>
#include <cmath>
#include <chrono>
using namespace std;
using namespace std::chrono;

struct Point {
    double x, y;
};

double distance(Point a, Point b) {
    return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

int main(int argc, char* argv[]) {
    auto start = high_resolution_clock::now();
    if (argc < 2) {
        cout << "Please specify the input file" << endl;
        return 1;
    }
    ifstream input(argv[1]);
    if (!input.is_open()) {
        cout << "Could not open the input file" << endl;
        return 1;
    }
    Point points[1000];
    int n = 0;
    while (input >> points[n].x >> points[n].y) n++;
    input.close();
    cout << n << endl;
    bool visited[1000] = { false };
    visited[0] = true;
    int current = 0;
    double total_distance = 0;
    for (int i = 1; i < n; i++) {
        double min_distance = INFINITY;
        int next = -1;
        for (int j = 0; j < n; j++) {
            if (!visited[j]) {
                double d = distance(points[current], points[j]);
                if (d < min_distance) {
                    min_distance = d;
                    next = j;
                }
            }
        }
        visited[next] = true;
        current = next;
        total_distance += min_distance;
    }
    total_distance += distance(points[current], points[0]);
    cout << total_distance << endl;
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << duration.count() / 1000000.0 << endl;
}