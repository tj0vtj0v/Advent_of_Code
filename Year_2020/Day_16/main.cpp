//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include <map>
#include "../Text.cpp"
#include "Ticket.h"
#include "Field.h"

using namespace std;


vector<Field> fields;
vector<Ticket> tickets;
vector<Ticket> validTickets;
Ticket ownTicket;

int readInput(const vector<string> &input) {
    int index = 0;

    while (!input.at(index).empty()) {
        fields.emplace_back(input.at(index));

        index++;
    }

    index += 2;

    ownTicket = Ticket(input.at(index));

    index += 3;

    while (index < input.size()) {
        auto ticket = Ticket(input.at(index));
        tickets.push_back(ticket);

        if (ticket.isValid()) {
            validTickets.push_back(ticket);
        }

        index++;
    }

    return 0;
}

int first(const vector<string> &input) {
    int errorRate = 0;

    for (auto ticket: tickets) {
        for (auto field: ticket.getFields()) {
            errorRate += Field::isInAnyRange(field) ? 0 : field;
        }
    }

    cout << errorRate;

    return 0;
}

vector<vector<int>> buildPossiblePositions() {
    vector<vector<int>> possiblePositions;

    for (int fieldID = 0; fieldID < fields.size(); fieldID++) {
        for (int fieldPos = 0; fieldPos < ownTicket.getFields().size(); fieldPos++) {
            bool allInRange = true;
            for (auto entry: Ticket::dataField(fieldPos)) {
                if (!(fields.at(fieldID).isInRange(entry))) {
                    allInRange = false;
                }
            }
            if (allInRange) {
                if (possiblePositions.size() <= fieldID) {
                    possiblePositions.emplace_back();
                }
                possiblePositions.at(fieldID).push_back(fieldPos);
            }
        }
    }

    return possiblePositions;
}

map<int, int> buildMap(const vector<vector<int>> &possiblePositions) {
    map<int, int> IDToPos;
    vector<int> usedPos;

    while (usedPos.size() < fields.size()) {
        for (int index = 0; index < possiblePositions.size(); index++) {
            vector<int> remainingPositions = {};

            for (auto position: possiblePositions.at(index)) {
                bool alreadyUsed = false;
                for (auto uPos: usedPos) {
                    if (position == uPos) {
                        alreadyUsed = true;
                    }
                }
                if (!alreadyUsed) {
                    remainingPositions.push_back(position);
                }
            }

            if (remainingPositions.size() == 1) {
                usedPos.push_back(remainingPositions.at(0));
                IDToPos[index] = remainingPositions.at(0);
            }
        }
    }

    return IDToPos;
}

int second(const vector<string> &input) {
    vector<vector<int>> possiblePositions = buildPossiblePositions();
    map<int, int> IDToPos = buildMap(possiblePositions);

    long long departureProduct = 1;
    for (int fieldID = 0; fieldID < fields.size(); fieldID++) {
        if (fields.at(fieldID).getName().find("departure") < fields.at(fieldID).getName().size()) {
            departureProduct *= ownTicket.getFields().at(IDToPos[fieldID]);
        }
    }

    cout << departureProduct;

    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_16");
    readInput(input);

    first(input);
    cout << endl;
    second(input);

    return 0;
}
