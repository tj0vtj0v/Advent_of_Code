//
// Created by Tjorven on 11.08.2024.
//

#include "HyperCube.h"

HyperCube::HyperCube(tuple<int, int, int, int> coordinate) {
    this->coordinate = coordinate;
}

bool HyperCube::operator==(HyperCube &other) {
    return coordinate == other.coordinate;
}

bool HyperCube::operator<(const HyperCube &other) const {
    return coordinate < other.coordinate;
}

tuple<int, int, int, int> HyperCube::getCoordinate() {
    return coordinate;
}

int HyperCube::getW() {
    return get<3>(coordinate);
}
