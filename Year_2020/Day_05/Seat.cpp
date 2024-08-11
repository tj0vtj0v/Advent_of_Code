//
// Created by Tjorven on 11.08.2024.
//

#include "Seat.h"

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
