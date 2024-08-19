//
// Created by Tjorven on 18.08.2024.
//

#ifndef YEAR_2020_FIELD_H
#define YEAR_2020_FIELD_H


#include <iostream>

using namespace std;

class Field {
public:
    explicit Field(const string &field);

    static bool isInAnyRange(int number);

    bool isInRange(int number);

    string getName();

private:
    static int allFirstStart;
    static int allFirstStop;
    static int allSecondStart;
    static int allSecondStop;

    string name;
    int position;
    int firstStart;
    int firstStop;
    int secondStart;
    int secondStop;
};

#include "Field.cpp"

#endif //YEAR_2020_FIELD_H
