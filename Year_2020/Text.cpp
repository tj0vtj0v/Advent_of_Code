//
// Created by tjorven on 06.08.24.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<string> read(const string& path) {
    string line;
    vector<string> text{};

    ifstream Input(path);
    while (getline(Input, line)) {
        text.push_back(line);
    }
    Input.close();

    return text;
}
