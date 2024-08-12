//
// Created by Tjorven on 11.08.2024.
//

#include "GameOfLife.h"

template<size_t V>
GameOfLife<V>::GameOfLife() {
    active = {};
}

template<size_t V>
unsigned long GameOfLife<V>::size() {
    return active.size();
}

template<size_t V>
int GameOfLife<V>::addActive(array<int, V> &cell) {
    active.push_back(cell);

    return 0;
}

template<size_t V>
int GameOfLife<V>::advanceGeneration() {
    auto haufen = createHaufen();
    active = determineSubsequentActiveCubes(haufen);

    return 0;
}

template<size_t V>
int GameOfLife<V>::advanceToGeneration(int generation) {
    for (int i = 0; i < generation; ++i) {
        advanceGeneration();
    }

    return 0;
}

template<size_t V>
Haufen<V> GameOfLife<V>::createHaufen() {
    Haufen<V> haufen = Haufen<V>();

    for (auto cell: this->active) {
        addNeighbours(haufen, V, cell, true);
    }

    return haufen;
}

template<size_t V>
int GameOfLife<V>::addNeighbours(Haufen<V> &haufen, int dimension, array<int, V> cell, bool allNull) {

    if (dimension > 0) {
        cell[V - dimension] -= 1;
        addNeighbours(haufen, dimension - 1, cell, false);
        cell[V - dimension] += 1;
        addNeighbours(haufen, dimension - 1, cell, allNull);
        cell[V - dimension] += 1;
        addNeighbours(haufen, dimension - 1, cell, false);
    } else if (!allNull) {
        haufen.addElement(cell);
    }

    return 0;
}

template<size_t V>
vector<array<int, V>> GameOfLife<V>::determineSubsequentActiveCubes(Haufen<V> &haufen) {
    vector<array<int, V>> nextActiveCubes;

    for (auto cube: haufen.getElementByOccurrence(2)) {
        for (auto livingCube: active) {
            if (cube == livingCube) {
                nextActiveCubes.push_back(cube);
            }
        }
    }

    for (auto cube: haufen.getElementByOccurrence(3)) {
        nextActiveCubes.push_back(cube);
    }

    return nextActiveCubes;
}
