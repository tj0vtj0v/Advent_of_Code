//
// Created by Tjorven on 11.08.2024.
//

#include "Bag.h"

Bag::Bag(const string &description) {
    string splitText = " bags contain ";
    int splitStart = description.find(splitText);

    type = description.substr(0, splitStart);
    content = description.substr(splitStart + splitText.length());
}

bool Bag::operator<(const Bag &other) const {
    return type < other.type;
}

string Bag::getType() {
    return type;
}

string Bag::getContent() {
    return content;
}

int Bag::addChild(Bag *bag, int quantity) {
    children[bag] = quantity;

    return 0;
}

int Bag::addParent(Bag *bag, int quantity) {
    parents[bag] = quantity;

    return 0;
}

set<Bag *> Bag::findParentBags(set<Bag *> found) {
    if (parents.empty()) {
        return found;
    }

    for (auto &parent: parents) {
        found = parent.first->findParentBags(found);
        if (found.count(parent.first) == 0) {
            found.insert(parent.first);
            found.merge(parent.first->findParentBags(found));
        }
    }

    return found;
}

int Bag::calculateInnerBags() {
    int a = 0;

    for (auto child: children) {
        a += child.second * (child.first->calculateInnerBags() + 1);
    }

    return a;
}
