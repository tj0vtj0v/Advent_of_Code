//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <tuple>

using namespace std;

#ifndef YEAR_2020_CUBE_H
#define YEAR_2020_CUBE_H


class Cube {
public:
    Cube();
    explicit Cube(tuple<int, int, int> coordinate);

    bool operator==(Cube &other);
    bool operator<(const Cube &other) const;

    tuple<int, int, int> getCoordinate();

    int getX();

    int getY();

    int getZ();

private:
    tuple<int, int, int> coordinate;
};


#endif //YEAR_2020_CUBE_H
