//
// Created by Tjorven on 18.08.2024.
//

#ifndef YEAR_2020_TICKET_H
#define YEAR_2020_TICKET_H


#include <iostream>
#include <vector>
#include <algorithm>
#include "Field.h"


using namespace std;

class Ticket {
public:
    Ticket() = default;

    explicit Ticket(string ticket);

    static vector<int> dataField(int fieldID);

    vector<int> getFields();

    bool isValid();

private:
    static vector<vector<int>> data;

    vector<int> fields;
};

#include "Ticket.cpp"

#endif //YEAR_2020_TICKET_H
