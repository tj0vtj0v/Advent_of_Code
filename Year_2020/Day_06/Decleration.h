//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <vector>
#include <set>

using namespace std;

#ifndef YEAR_2020_DECLERATION_H
#define YEAR_2020_DECLERATION_H


class Decleration {
public:
    explicit Decleration(const vector<string> &group);

    unsigned long affirmedQuestions();

    int collectivelyAffirmedQuestions();

private:
    int groupSize = 0;
    vector<char> affirmed;
    set<char> affirmedWithoutDoublicates;
};


#endif //YEAR_2020_DECLERATION_H
