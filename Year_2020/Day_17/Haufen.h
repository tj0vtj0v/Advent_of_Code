//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <vector>
#include <map>

using namespace std;

#ifndef YEAR_2020_HAUFEN_H
#define YEAR_2020_HAUFEN_H

template <class D>
class Haufen {
public:
    Haufen();

    int addElement(D cube);

    vector<D> getElementByOccurrence(int occurrence);

private:
    map<D, int> haufen;
};

#include "Haufen.tpp"

#endif //YEAR_2020_HAUFEN_H
