//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"

using namespace std;

int first(const vector<string>& input) {

    for (int current = 0; current < input.size(); current++) {
        for (int number = current + 1; number < input.size(); number++) {
            if (stoi(input.at(current)) + stoi(input.at(number)) == 2020) {
                cout << stoi(input.at(current)) * stoi(input.at(number));
                return 0;
            }
        }
    }

    return 1;
}

int second(const vector<string>& input) {

    for (int first_number = 0; first_number < input.size(); first_number++) {
        for (int second_number = first_number + 1; second_number < input.size(); second_number++) {
            for (int third_number = second_number + 1; third_number < input.size(); third_number++) {
                if (stoi(input.at(first_number)) + stoi(input.at(second_number)) + stoi(input.at(third_number)) == 2020) {
                    cout << stoi(input.at(first_number)) * stoi(input.at(second_number)) * stoi(input.at(third_number));
                    return 0;
                }
            }
        }
    }

    return 1;
}

int main() {
    const vector<string> input = read("../Input/Day_01");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
