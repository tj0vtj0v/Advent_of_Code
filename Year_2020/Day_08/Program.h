//
// Created by Tjorven on 11.08.2024.
//

#ifndef YEAR_2020_PROGRAM_H
#define YEAR_2020_PROGRAM_H


#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

class Program {
public:
    explicit Program(const vector<string> &input);

    int getAccumulator();

    int resetAccumulator();

    int executeLine(int lineOfCode);

    int executeChangedLine(int lineOfCode);

    int length();

private:
    int executeNOP(int lineOfCode);

    int executeJMP(int lineOfCode, tuple<string, int> &command);

    int executeACC(int lineOfCode, tuple<string, int> &command);

    vector<tuple<string, int> > commands;
    int accumulator;
};

#include "Program.cpp"

#endif //YEAR_2020_PROGRAM_H
