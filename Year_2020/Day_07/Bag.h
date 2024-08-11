//
// Created by Tjorven on 11.08.2024.
//

#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;

#ifndef YEAR_2020_BAG_H
#define YEAR_2020_BAG_H


class Bag {
public:
    explicit Bag(const string &description);

    bool operator<(const Bag &other) const;

    string getType();

    string getContent();

    int addChild(Bag *bag, int quantity);

    int addParent(Bag *bag, int quantity);

    set<Bag *> findParentBags(set<Bag *> found);

    int calculateInnerBags();

private:
    string type;
    string content;
    map<Bag *, int> children = {};
    map<Bag *, int> parents = {};
};


#endif //YEAR_2020_BAG_H
