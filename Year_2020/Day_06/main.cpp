//
// Created by tjorven on 07.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "Decleration.h"

using namespace std;

vector<Decleration> createDeclerations(const vector<string> &input) {
    vector<Decleration> declerations;

    vector<string> current;
    for (const auto &line: input) {
        current.push_back(line);
        if (line.empty()) {
            declerations.emplace_back(current);
            current.clear();
        }
    }
    declerations.emplace_back(current);

    return declerations;
}

int first(const vector<string> &input) {
    vector<Decleration> declerations = createDeclerations(input);
    unsigned long affirmationCount = 0;

    for (auto decleration: declerations) {
        affirmationCount += decleration.affirmedQuestions();
    }

    cout << affirmationCount;
    return 0;
}

int second(const vector<string> &input) {
    vector<Decleration> declerations = createDeclerations(input);
    unsigned long affirmationCount = 0;

    for (auto decleration: declerations) {
        affirmationCount += decleration.collectivelyAffirmedQuestions();
    }

    cout << affirmationCount;
    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_06");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
