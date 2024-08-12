//
// Created by Tjorven on 11.08.2024.
//

#include "Haufen.h"

template <size_t V>
Haufen<V>::Haufen() = default;

template <size_t V>
int Haufen<V>::addElement(array<int, V> cell) {
    if (haufen.count(cell) == 0) {
        haufen[cell] = 1;
    } else {
        haufen[cell] = haufen[cell] + 1;
    }

    return 0;
}

template <size_t V>
vector<array<int, V>> Haufen<V>::getElementByOccurrence(int occurrence) {
    vector<array<int, V>> cubes;

    for (auto &entry: haufen) {
        if (entry.second == occurrence) {
            cubes.push_back(entry.first);
        }
    }

    return cubes;
}
