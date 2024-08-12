//
// Created by Tjorven on 11.08.2024.
//

#ifndef YEAR_2020_MAP_H
#define YEAR_2020_MAP_H


#include <iostream>
#include <vector>

using namespace std;


class Map {
public:
    explicit Map(const vector<string> &input);

    int encounteredTreesWithSlope(int step_x, int step_y);

private:
    bool treeAtPosition(int x, int y);

    vector<string> map;
};

#include "Map.cpp"

#endif //YEAR_2020_MAP_H
