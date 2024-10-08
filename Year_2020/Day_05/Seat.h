//
// Created by Tjorven on 11.08.2024.
//

#ifndef YEAR_2020_SEAT_H
#define YEAR_2020_SEAT_H


#include <iostream>
#include <cmath>

using namespace std;


class Seat {
public:
    explicit Seat(const string &explanation);

    bool operator<(const Seat &other) const;

    double getRow();

    double getColumn();

    double getID();

private:
    double row = 0;
    double col = 0;
    double ID;
};

#include "Seat.cpp"

#endif //YEAR_2020_SEAT_H
