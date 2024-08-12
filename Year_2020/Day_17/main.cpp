//
// Created by tjorven on 09.08.24.
//

#include <iostream>
#include <vector>
#include "../Text.cpp"
#include "ConwayCube.h"
#include "ConwayHyperCube.h"

using namespace std;

ConwayCube createCube(const vector<string> &input) {
    auto conwayCube = ConwayCube();

    int z = 0;
    for (int y = 0; y < input.size(); ++y) {
        for (int x = 0; x < input.at(0).size(); ++x) {
            if (input.at(y).at(x) == '#') {
                auto found = Cube({x, y, z});
                conwayCube.addActive(found);
            }
        }
    }

    return conwayCube;
}

ConwayHyperCube createHyperCube(const vector<string> &input) {
    auto conwayCube = ConwayHyperCube();

    int w = 0;
    int z = 0;
    for (int y = 0; y < input.size(); ++y) {
        for (int x = 0; x < input.at(0).size(); ++x) {
            if (input.at(y).at(x) == '#') {
                auto found = HyperCube({x, y, z, w});
                conwayCube.addActive(found);
            }
        }
    }

    return conwayCube;
}

int first(const vector<string> &input) {
    ConwayCube cube = createCube(input);

    cube.advanceToGeneration(6);

    cout << cube.size();

    return 0;
}

int second(const vector<string> &input) {
    ConwayHyperCube hyperCube = createHyperCube(input);

    hyperCube.advanceToGeneration(6);

    cout << hyperCube.size();

    return 0;
}

int main() {
    const vector<string> input = read("../Input/Day_17");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
