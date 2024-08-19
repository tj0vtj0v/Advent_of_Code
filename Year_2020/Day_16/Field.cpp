//
// Created by Tjorven on 18.08.2024.
//

#include "Field.h"

int Field::allFirstStart = 999;
int Field::allFirstStop = 0;
int Field::allSecondStart = 999;
int Field::allSecondStop = 0;

Field::Field(const string &field) {
    int separator = field.find(": ");
    name = field.substr(0, separator);
    position = -1;

    separator += 2;
    string range = field.substr(separator, field.find(" or ") - separator);
    firstStart = stoi(range.substr(0, range.find('-')));
    firstStop = stoi(range.substr(range.find('-')+1));

    range = field.substr(field.find(" or ") + 4);
    secondStart = stoi(range.substr(0, range.find('-')));
    secondStop = stoi(range.substr(range.find('-')+1));

    allFirstStart = allFirstStart > firstStart ? firstStart : allFirstStart;
    allFirstStop = allFirstStop < firstStop ? firstStop : allFirstStop;
    allSecondStart = allSecondStart > secondStart ? secondStart : allSecondStart;
    allSecondStop = allSecondStop < secondStop ? secondStop : allSecondStop;
}

bool Field::isInRange(int number) {
    bool inFirst = firstStart <= number && number <= firstStop;
    bool inSecond = secondStart <= number && number <= secondStop;

    return inFirst || inSecond;
}

bool Field::isInAnyRange(int number) {
    bool inFirst = allFirstStart <= number && number <= allFirstStop;
    bool inSecond = allSecondStart <= number && number <= allSecondStop;

    return inFirst || inSecond;
}

string Field::getName() {
    return name;
}
