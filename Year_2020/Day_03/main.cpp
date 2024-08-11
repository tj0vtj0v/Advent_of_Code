//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"

using namespace std;


class Map {
public:
    explicit Map(const vector<string> &input);

    int encounteredTreesWithSlope(int step_x, int step_y);

private:
    bool treeAtPosition(int x, int y);

    vector<string> map;
};

Map::Map(const vector<string> &input) {
    this->map = input;
}

bool Map::treeAtPosition(const int x, const int y) {
    return map.at(y).at(x % map.at(0).length()) == '#';
}

int Map::encounteredTreesWithSlope(int step_x, int step_y) {
    int x = 0;
    int y = 0;
    int encounteredTrees = 0;

    while (y < map.size()) {
        encounteredTrees += treeAtPosition(x, y);

        x += step_x;
        y += step_y;
    }

    return encounteredTrees;
}


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
    const vector<string> input = read("Input/Day_03");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
