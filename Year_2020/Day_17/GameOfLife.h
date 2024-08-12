//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <vector>
#include "Haufen.h"

using namespace std;

#ifndef YEAR_2020_GAMEOFLIFE_H
#define YEAR_2020_GAMEOFLIFE_H

template<size_t V>
class GameOfLife {
public:
    explicit GameOfLife();

    unsigned long size();

    int addActive(array<int, V> &cell);

    int advanceGeneration();

    int advanceToGeneration(int generation);

protected:
    Haufen<V> createHaufen();

    int addNeighbours(Haufen<V> &haufen, int dimension, array<int, V> cell, bool allNull);

    vector<array<int, V>> determineSubsequentActiveCubes(Haufen<V> &haufen);

    vector<array<int, V>> active;
};

#include "GameOfLife.tpp"

#endif //YEAR_2020_GAMEOFLIFE_H
