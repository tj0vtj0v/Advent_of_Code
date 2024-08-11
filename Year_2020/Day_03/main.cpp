//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "Map.h"

using namespace std;

int first(const vector<string> &input) {
    auto map = Map(input);
    cout << map.encounteredTreesWithSlope(3, 1);

    return 0;
}

int second(const vector<string> &input) {
    auto map = Map(input);
    long long result = map.encounteredTreesWithSlope(1, 1);
    result *= map.encounteredTreesWithSlope(3, 1);
    result *= map.encounteredTreesWithSlope(5, 1);
    result *= map.encounteredTreesWithSlope(7, 1);
    result *= map.encounteredTreesWithSlope(1, 2);

    cout << result;
    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_03");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
