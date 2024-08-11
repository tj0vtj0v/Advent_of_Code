//
// Created by tjorven on 07.08.24.
//

#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include "../Text.cpp"

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

Seat::Seat(const string &explanation) {
    string rowExplanation = explanation.substr(0, explanation.size() - 3);
    string colExplanation = explanation.substr(explanation.size() - 3, explanation.size());

    for (int index = 0; index < rowExplanation.size(); index++) {
        if (rowExplanation.at(index) == 'B') {
            row += pow(2, rowExplanation.size() - index - 1);
        }
    }

    for (int index = 0; index < colExplanation.size(); index++) {
        if (colExplanation.at(index) == 'R') {
            col += pow(2, colExplanation.size() - index - 1);
        }
    }

    ID = row * 8 + col;
}

bool Seat::operator<(const Seat &other) const {
    return ID < other.ID;
}

double Seat::getRow() {
    return row;
}

double Seat::getColumn() {
    return col;
}

double Seat::getID() {
    return ID;
}


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
    const vector<string> input = read("Input/Day_05");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
