//
// Created by Tjorven on 11.08.2024.
//

#ifndef YEAR_2020_PASSPORT_H
#define YEAR_2020_PASSPORT_H


#include <unordered_map>

using namespace std;

class Passport {
public:
    explicit Passport(const vector<string> &lines);

    bool isValidAccordingToRuleOne();

    bool isValidAccordingToRuleTwo();

private:
    unordered_map<string, string> fields;
};

#include "Passport.cpp"

#endif //YEAR_2020_PASSPORT_H
