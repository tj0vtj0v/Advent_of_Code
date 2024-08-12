//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <vector>
#include <map>

using namespace std;

#ifndef YEAR_2020_HAUFEN_H
#define YEAR_2020_HAUFEN_H

template <size_t V>
class Haufen {
public:
    Haufen();

    int addElement(array<int, V> cell);

    vector<array<int, V>> getElementByOccurrence(int occurrence);

private:
    map<array<int, V>, int> haufen;
};

#include "Haufen.tpp"

#endif //YEAR_2020_HAUFEN_H
