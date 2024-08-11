//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <cmath>

using namespace std;

#ifndef YEAR_2020_SEAT_H
#define YEAR_2020_SEAT_H


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


#endif //YEAR_2020_SEAT_H
