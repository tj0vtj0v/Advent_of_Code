//
// Created by Tjorven on 18.08.2024.
//

#include "Ticket.h"

vector<vector<int>> Ticket::data;

Ticket::Ticket(string ticket) {
    while (ticket.find(',') < ticket.length()) {
        fields.push_back(stoi(ticket.substr(0, ticket.find(','))));
        ticket = ticket.substr(ticket.find(',') + 1);
    }
    fields.push_back(stoi(ticket));


    while (data.size() < fields.size()) {
        data.emplace_back();
    }
    if (this->isValid()) {
    for (int field = 0; field < fields.size(); field++) {
        data.at(field).push_back(fields.at(field));
    }}
}

bool Ticket::isValid() {
    if (all_of(fields.begin(), fields.end(), [](int i){return Field::isInAnyRange(i);})) {
        return true;
    }
    return false;
}

vector<int> Ticket::dataField(int fieldID) {
    return data.at(fieldID);
}

vector<int> Ticket::getFields() {
    return fields;
}
