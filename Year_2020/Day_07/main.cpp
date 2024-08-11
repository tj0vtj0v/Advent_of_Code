//
// Created by tjorven on 07.08.24.
//

#include <iostream>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include "../Text.cpp"

class Bag;
class Content;

using namespace std;


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

int manageBag(Bag *bag, const string &currentBag, vector<Bag> &bags) {
    if (currentBag.substr(0, 1).find_first_not_of("0123456789") < 1) {
        return 0;
    }

    int amount = stoi(currentBag.substr(0, currentBag.find(' ')));
    string type = currentBag.substr(currentBag.find(' ') + 1);

    for (auto &bagToCopy: bags) {
        if (bagToCopy.getType() == type) {
            bag->addChild(&bagToCopy, amount);
            bagToCopy.addParent(bag, amount);
            break;
        }
    }

    return 0;
}

int manageContents(vector<Bag> &bags) {
    for (auto &bag: bags) {
        string rest = bag.getContent();
        string currentBag;

        while (rest.find(" bag") < rest.size()) {
            currentBag = rest.substr(0, rest.find(" bag"));

            manageBag(&bag, currentBag, bags);

            if (rest.find(", ") < rest.size()) {
                rest = rest.substr(rest.find(", ") + 2);
            } else {
                break;
            }
        }
    }

    return 0;
}

vector<Bag> createBags(const vector<string> &input) {
    vector<Bag> bags;
    bags.reserve(input.size());

    for (const auto &line: input) {
        bags.emplace_back(line);
    }

    manageContents(bags);

    return bags;
}

int first(const vector<string> &input) {
    vector<Bag> bags = createBags(input);

    for (auto &bag: bags) {
        if (bag.getType() == "shiny gold") {
            cout << bag.findParentBags({}).size();

            return 0;
        }
    }

    return 0;
}

int second(const vector<string> &input) {
    vector<Bag> bags = createBags(input);

    for (auto &bag: bags) {
        if (bag.getType() == "shiny gold") {
            cout << bag.calculateInnerBags();

            return 0;
        }
    }

    return 0;
}

int main() {
    const vector<string> input = read("Input/Day_07");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
