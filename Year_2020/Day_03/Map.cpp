//
// Created by Tjorven on 11.08.2024.
//

#include "Map.h"

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