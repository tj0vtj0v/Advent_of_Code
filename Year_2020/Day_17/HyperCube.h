//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <tuple>
#include "Cube.h"

using namespace std;

#ifndef YEAR_2020_HYPERCUBE_H
#define YEAR_2020_HYPERCUBE_H


class HyperCube: public Cube{
public:
    explicit HyperCube(tuple<int, int, int, int> a);

    bool operator==(HyperCube &other);
    bool operator<(const HyperCube &other) const;

    tuple<int, int, int, int> getCoordinate();

    int getW();

private:
    tuple<int, int, int, int> coordinate;
};


#endif //YEAR_2020_HYPERCUBE_H
