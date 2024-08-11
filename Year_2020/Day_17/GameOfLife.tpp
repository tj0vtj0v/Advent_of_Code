//
// Created by Tjorven on 11.08.2024.
//

#include "GameOfLife.h"

template <class D>
GameOfLife<D>::GameOfLife() {
    active = {};
}

template <class D>
unsigned long GameOfLife<D>::size() {
    return active.size();
}

template <class D>
int GameOfLife<D>::addActive(D &cell) {
    active.push_back(cell);

    return 0;
}

template <class D>
int GameOfLife<D>::advanceGeneration() {
    auto haufen = createHaufen();
    active = determineSubsequentActiveCubes(haufen);

    return 0;
}

template <class D>
int GameOfLife<D>::advanceToGeneration(int generation) {
    for (int i = 0; i < generation; ++i) {
        advanceGeneration();
    }

    return 0;
}

template <class D>
vector<D> GameOfLife<D>::determineSubsequentActiveCubes(Haufen<D> &haufen) {
    vector<D> nextActiveCubes;

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
