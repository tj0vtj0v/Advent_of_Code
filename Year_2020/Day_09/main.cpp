//
// Created by Tjorven on 12.08.2024.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "Buffer.h"

using namespace std;

Buffer createFilledBuffer(int capacity, const vector<string> &input) {
    auto buffer = Buffer(capacity);

    for (int i = 0; i < capacity; ++i) {
        buffer.insertNumber(stol(input.at(i)));
    }

    return buffer;
}

long first(const vector<string> &input) {
    auto buffer = createFilledBuffer(25, input);

    for (int index = buffer.size(); index < input.size(); ++index) {

        long number = stoll(input.at(index));
        if (buffer.dualCombination(number)) {

            buffer.insertNumber(number);
        } else {
            cout << number;
            return number;
        }
    }

    return 0;
}


int second(const vector<string> &input) {
    long target = 1639024365; // result from first

    for (int length = 2; length < input.size(); ++length) {
        auto buffer = createFilledBuffer(length, input);

        int index = length;
        while (index < input.size()) {
            if (buffer.sum() == target) {
                cout << buffer.max() + buffer.min() << endl;

                return 0;
            }
            buffer.insertNumber(stoll(input.at(index)));

            index++;
        }
    }
    return 0;
}

int main() {
    vector<string> input = read("../Input/Day_09");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
