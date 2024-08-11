//
// Created by Tjorven on 11.08.2024.
//

#include "Haufen.h"

template <class D>
Haufen<D>::Haufen() = default;

template <class D>
int Haufen<D>::addElement(D cube) {
    if (haufen.count(cube) == 0) {
        haufen[cube] = 1;
    } else {
        haufen[cube] = haufen[cube] + 1;
    }

    return 0;
}

template <class D>
vector<D> Haufen<D>::getElementByOccurrence(int occurrence) {
    vector<D> cubes;

    for (auto &entry: haufen) {
        if (entry.second == occurrence) {
            cubes.push_back(entry.first);
        }
    }

    return cubes;
}
