//
// Created by tjorven on 09.08.24.
//

#include <iostream>
#include <vector>
#include <array>
#include "../Text.cpp"
#include "GameOfLife.h"

using namespace std;

template<size_t V>
GameOfLife<V> createGameFromPlane(const vector<string> &input) {
    GameOfLife<V> game = GameOfLife<V>();

    array<int, V> nullCell{};
    nullCell.fill(0);
    for (int y = 0; y < input.size(); ++y) {
        for (int x = 0; x < input.at(0).size(); ++x) {
            if (input.at(y).at(x) == '#') {
                array<int, V> cell = nullCell;
                cell[0] = x;
                cell[1] = y;
                game.addActive(cell);
            }
        }
    }

    return game;
}


int first(const vector<string> &input) {
    auto game = createGameFromPlane<3>(input);

    game.advanceToGeneration(6);

    cout << game.size();

    return 0;
}

int second(const vector<string> &input) {
    auto game = createGameFromPlane<4>(input);

    game.advanceToGeneration(6);

    cout << game.size();

    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_17");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
