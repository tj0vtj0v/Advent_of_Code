//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"

using namespace std;

// to put in own file Password.h
class Password {
public:
    explicit Password(const string &entry);

    bool isValidAccordingToPolicyOne();

    bool isValidAccordingToPolicyTwo();

private:
    string all;
    string password;
    char letter;
    int first_number;
    int second_number;
};

// to put in own file Password.cpp
Password::Password(const string &entry) {
    all = entry;
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
// end of seperate file content

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
    const vector<string> input = read("Input/Day_02");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
