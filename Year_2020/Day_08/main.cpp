//
// Created by tjorven on 09.08.24.
//

#include <iostream>
#include <set>
#include <vector>
#include "../Text.cpp"
#include "Program.h"

using namespace std;

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
    const vector<string> input = read("../Input/Day_08");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
