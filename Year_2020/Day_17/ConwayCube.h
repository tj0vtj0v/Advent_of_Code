//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include "Cube.h"
#include "GameOfLife.h"

#ifndef YEAR_2020_CONWAYCUBE_H
#define YEAR_2020_CONWAYCUBE_H


class ConwayCube: public GameOfLife<Cube>{
public:
    explicit ConwayCube();

protected:
    Haufen<Cube> createHaufen();
};

#include "ConwayCube.tpp"

#endif //YEAR_2020_CONWAYCUBE_H
