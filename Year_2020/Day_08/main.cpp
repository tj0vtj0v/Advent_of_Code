//
// Created by tjorven on 09.08.24.
//

#include <iostream>
#include <map>
#include <set>
#include <vector>
#include "../Text.cpp"

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


int bruteForceChanges(Program &program) {
    int changedLine = 0;

    while (true) {
        set<int> executed;
        int lineOfCode = 0;
        int executedLines = 0;

        while (executed.count(lineOfCode) == 0 && lineOfCode < program.length()) {
            executed.insert(lineOfCode);

            if (executedLines == changedLine) {
                lineOfCode = program.executeChangedLine(lineOfCode);
            } else {
                lineOfCode = program.executeLine(lineOfCode);
            }

            executedLines++;
        }

        if (lineOfCode == program.length()) {
            break;
        }

        program.resetAccumulator();
        changedLine++;
    }

    return 0;
}

int first(const vector<string> &input) {
    auto program = Program(input);

    set<int> executed;
    int lineOfCode = 0;


    while (executed.count(lineOfCode) == 0) {
        executed.insert(lineOfCode);

        lineOfCode = program.executeLine(lineOfCode);
    }

    cout << program.getAccumulator();

    return 0;
}

int second(const vector<string> &input) {
    auto program = Program(input);

    bruteForceChanges(program);

    cout << program.getAccumulator();

    return 0;
}

int main() {
    const vector<string> input = read("Input/Day_08");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
