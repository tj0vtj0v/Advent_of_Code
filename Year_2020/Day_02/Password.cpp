//
// Created by Tjorven on 11.08.2024.
//

#include "Password.h"

Password::Password(const string &entry) {
    string policy = entry.substr(0, entry.find(':'));

    password = entry.substr(entry.find(':') + 2);
    letter = policy.at(policy.length() - 1);

    string amount = policy.substr(0, policy.find(' '));

    first_number = stoi(amount.substr(0, amount.find('-')));
    second_number = stoi(amount.substr(amount.find('-') + 1, amount.length()));
}

bool Password::isValidAccordingToPolicyOne() {
    int letter_count = 0;

    for (const char character: password) {
        if (character == letter) {
            letter_count++;
        }
    }

    return first_number <= letter_count && letter_count <= second_number;
}

bool Password::isValidAccordingToPolicyTwo() {
    return (password.at(first_number - 1) == letter) != (password.at(second_number - 1) == letter);
}