//
// Created by Tjorven on 11.08.2024.
//

#ifndef YEAR_2020_PASSWORD_H
#define YEAR_2020_PASSWORD_H


#include <iostream>

using namespace std;

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

#include "Password.cpp"

#endif //YEAR_2020_PASSWORD_H
