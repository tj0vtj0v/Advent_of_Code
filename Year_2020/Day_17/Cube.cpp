//
// Created by Tjorven on 11.08.2024.
//

#include "Cube.h"

Cube::Cube() = default;

Cube::Cube(tuple<int, int, int> coordinate) {
    this->coordinate = coordinate;
}

bool Cube::operator==(Cube &other) {
    return coordinate == other.coordinate;
}

bool Cube::operator<(const Cube &other) const {
    return coordinate < other.coordinate;
}

tuple<int, int, int> Cube::getCoordinate() {
    return coordinate;
}

int Cube::getX() {
    return get<0>(coordinate);
}

int Cube::getY() {
    return get<1>(coordinate);
}

int Cube::getZ() {
    return get<2>(coordinate);
}
