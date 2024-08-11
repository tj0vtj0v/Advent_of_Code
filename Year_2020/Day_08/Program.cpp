//
// Created by Tjorven on 11.08.2024.
//

#include "Program.h"

Program::Program(const vector<string> &input) {
    accumulator = 0;
    for (const auto &line: input) {
        commands.emplace_back(line.substr(0, 3), stoi(line.substr(line.find(' '))));
    }
}

int Program::getAccumulator() {
    return accumulator;
}

int Program::resetAccumulator() {
    accumulator = 0;

    return 0;
}

int Program::executeLine(int lineOfCode) {
    auto command = commands.at(lineOfCode);

    if (get<0>(command) == "nop") {
        return executeNOP(lineOfCode);
    }
    if (get<0>(command) == "jmp") {
        return executeJMP(lineOfCode, command);
    }
    if (get<0>(command) == "acc") {
        return executeACC(lineOfCode, command);
    }

    return -1;
}

int Program::executeChangedLine(int lineOfCode) {
    auto command = commands.at(lineOfCode);

    if (get<0>(command) == "nop") {
        return executeJMP(lineOfCode, command);
    }
    if (get<0>(command) == "jmp") {
        return executeNOP(lineOfCode);
    }
    if (get<0>(command) == "acc") {
        return executeACC(lineOfCode, command);
    }

    return -1;
}

int Program::length() {
    return commands.size();
}

int Program::executeNOP(int lineOfCode) {
    return lineOfCode + 1;
}

int Program::executeJMP(int lineOfCode, tuple<string, int> &command) {
    return lineOfCode + get<1>(command);
}

int Program::executeACC(int lineOfCode, tuple<string, int> &command) {
    accumulator += get<1>(command);
    return lineOfCode + 1;
}
