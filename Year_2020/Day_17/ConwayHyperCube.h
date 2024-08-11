//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include "HyperCube.h"
#include "GameOfLife.h"

#ifndef YEAR_2020_CONWAYHYPERCUBE_H
#define YEAR_2020_CONWAYHYPERCUBE_H


class ConwayHyperCube: public GameOfLife<HyperCube>{
public:
    explicit ConwayHyperCube();

protected:
    Haufen<HyperCube> createHaufen();
};

#include "ConwayHyperCube.tpp"

#endif //YEAR_2020_CONWAYHYPERCUBE_H
