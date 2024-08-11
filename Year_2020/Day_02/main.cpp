//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "Password.h"

using namespace std;

int first(const vector<string> &input) {
    int valid_passwords = 0;

    for (const auto &entry: input) {
        auto password = Password(entry);
        valid_passwords += password.isValidAccordingToPolicyOne();
    }

    cout << valid_passwords;
    return 0;
}

int second(const vector<string> &input) {
    int valid_passwords = 0;

    for (const auto &entry: input) {
        auto password = Password(entry);
        valid_passwords += password.isValidAccordingToPolicyTwo();
    }

    cout << valid_passwords;
    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_02");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
