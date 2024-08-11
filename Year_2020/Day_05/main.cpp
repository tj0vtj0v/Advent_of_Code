//
// Created by tjorven on 07.08.24.
//

#include <iostream>
#include <vector>
#include <algorithm>
#include "../Text.cpp"
#include "Seat.h"

using namespace std;

vector<Seat> assignSeats(const vector<string> &input) {
    vector<Seat> seats;
    seats.reserve(input.size());
    for (const auto &line: input) {
        seats.emplace_back(line);
    }
    return seats;
}

int first(const vector<string> &input) {
    vector<Seat> seats = assignSeats(input);

    double maximumSeatID = 0;

    for (auto seat: seats) {
        maximumSeatID = maximumSeatID < seat.getID() ? seat.getID() : maximumSeatID;
    }

    cout << maximumSeatID;
    return 0;
}

int second(const vector<string> &input) {
    vector<Seat> seats = assignSeats(input);
    sort(seats.begin(), seats.end());

    double lastID = seats.at(0).getID() - 1;
    for (auto seat: seats) {
        if (lastID + 1 != seat.getID()) {
            cout << seat.getID() - 1;
        }

        lastID = seat.getID();
    }

    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_05");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
