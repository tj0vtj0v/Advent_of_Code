//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "MathQueue.h"

using namespace std;

vector<MathQueue> buildMathData(const vector<string> &input) {
    vector<MathQueue> mathData;

    mathData.reserve(input.size());
    for (const auto &expression: input) {
        mathData.emplace_back(expression);
    }

    return mathData;
}

int first(const vector<string> &input) {
    auto mathData = buildMathData(input);
    long long result = 0;

    for (auto problem : mathData) {
        result += problem.evaluate();
    }

    cout << result;

    return 0;
}

int second(const vector<string> &input) {
    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_18");

    first(input); //6396000287 l
    cout << endl;
    second(input);

    return 0;
}
