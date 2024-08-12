//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "Passport.h"

using namespace std;

vector<Passport> createPassports(const vector<string> &text) {
    vector<Passport> passports;

    vector<string> current;
    for (const string &line: text) {
        current.push_back(line);
        if (line.empty()) {
            passports.emplace_back(current);
            current.clear();
        }
    }
    passports.emplace_back(current);

    return passports;
}


int first(const vector<string> &input) {
    const vector<Passport> passports = createPassports(input);

    int validPassports = 0;

    for (auto passport: passports) {
        validPassports += passport.isValidAccordingToRuleOne();
    }

    cout << validPassports;

    return 0;
}

int second(const vector<string> &input) {
    const vector<Passport> passports = createPassports(input);

    int validPassports = 0;

    for (auto passport: passports) {
        validPassports += passport.isValidAccordingToRuleTwo();
    }

    cout << validPassports;

    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_04");


    first(input);
    cout << endl;
    second(input);

    return 0;
    // zw. 129 - 147 excl.
}
