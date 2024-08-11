//
// Created by tjorven on 09.08.24.
//

#include <time.h>

#include <iostream>
#include <map>
#include <vector>
#include <tuple>
#include "../Text.cpp"

using namespace std;

class Cube {
public:
    explicit Cube(tuple<int, int, int> coordinate);

    bool operator==(Cube &other);
    bool operator<(const Cube &other) const;

    tuple<int, int, int> getCoordinate();

    int getX();

    int getY();

    int getZ();

private:
    tuple<int, int, int> coordinate;
};


Cube::Cube(tuple<int, int, int> coordinate) {
    this->coordinate = coordinate;
}

bool Cube::operator==(Cube &other) {
    return getX() == other.getX() && getY() == other.getY() && getZ() == other.getZ();
}

bool Cube::operator<(const Cube &other) const {
    return coordinate < other.coordinate;
}


tuple<int, int, int> Cube::getCoordinate() {
    return coordinate;
}

int Cube::getX() {
    return get<0>(coordinate);
}

int Cube::getY() {
    return get<1>(coordinate);
}

int Cube::getZ() {
    return get<2>(coordinate);
}


class Haufen {
public:
    Haufen();

    int addCube(Cube cube);

    vector<Cube> getCubesByOccurence(int occurence);

private:
    map<Cube, int> haufen;
};


Haufen::Haufen() = default;

int Haufen::addCube(Cube cube) {
    if (haufen.count(cube) == 0) {
        haufen[cube] = 1;
    } else {
        haufen[cube] = haufen[cube] + 1;
    }

    return 0;
}

vector<Cube> Haufen::getCubesByOccurence(int occurence) {
    vector<Cube> cubes;

    for (auto &entry: haufen) {
        if (entry.second == occurence) {
            cubes.push_back(entry.first);
        }
    }

    return cubes;
}


class ConwayCube {
public:
    explicit ConwayCube();

    unsigned long size();

    int addCube(Cube &cube);

    int advanceGeneration();

private:
    vector<Cube> living;
};


ConwayCube::ConwayCube() = default;

unsigned long ConwayCube::size() {
    return living.size();
}

int ConwayCube::addCube(Cube &cube) {
    living.push_back(cube);

    return 0;
}

int ConwayCube::advanceGeneration() {
    vector<Cube> livingNextGeneration;
    auto haufen = Haufen();

    for (auto cube: living) {
        for (int x = -1; x <= 1; x++) {
            for (int y = -1; y <= 1; y++) {
                for (int z = -1; z <= 1; z++) {
                    auto toAdd = Cube({cube.getX() + x, cube.getY() + y, cube.getZ() + z});
                    if (x != 0 || y != 0 || z != 0) {
                        haufen.addCube(toAdd);
                    }
                }
            }
        }
    }

    for (auto cube: haufen.getCubesByOccurence(2)) {
        for (auto livingCube: living) {
            if (cube == livingCube) {
                livingNextGeneration.push_back(cube);
            }
        }
    }

    for (auto cube: haufen.getCubesByOccurence(3)) {
        livingNextGeneration.push_back(cube);
    }

    living = livingNextGeneration;

    return 0;
}


ConwayCube createCube(const vector<string> &input) {
    auto cube = ConwayCube();

    int z = 0;
    for (int y = 0; y < input.size(); ++y) {
        for (int x = 0; x < input.at(0).size(); ++x) {
            if (input.at(y).at(x) == '#') {
                auto found = Cube({x, y, z});
                cube.addCube(found);
            }
        }
    }

    return cube;
}


int first(const vector<string> &input) {
    ConwayCube cube = createCube(input);

    for (int i = 0; i < 50; ++i) {
        cube.advanceGeneration();
        cout << i << ": finished." << endl;
    }

    cout << cube.size() << endl;

    return 0;
}

int second(const vector<string> &input) {
    return 0;
}

int main() {
    const vector<string> input = read("Input/Day_17");


    first(input);
    cout << endl;
    second(input);

    return 0;
}
