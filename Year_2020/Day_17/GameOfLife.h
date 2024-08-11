//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <vector>
#include "Haufen.h"
#include "Cube.h"
#include "HyperCube.h"

using namespace std;

#ifndef YEAR_2020_GAMEOFLIFE_H
#define YEAR_2020_GAMEOFLIFE_H

template<class D>
class GameOfLife {
public:
    explicit GameOfLife();

    unsigned long size();

    int addActive(D &cell);

    int advanceGeneration();

    int advanceToGeneration(int generation);

protected:
    Haufen<D> createHaufen() { return Haufen<D>(); };

    vector<D> determineSubsequentActiveCubes(Haufen<D> &haufen);

    vector<D> active;
};

#include "GameOfLife.tpp"

#endif //YEAR_2020_GAMEOFLIFE_H
