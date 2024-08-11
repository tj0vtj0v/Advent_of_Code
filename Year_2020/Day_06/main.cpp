//
// Created by tjorven on 07.08.24.
//

#include <iostream>
#include <set>
#include <vector>
#include "../Text.cpp"

using namespace std;

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

Decleration::Decleration(const vector<string> &group) {
    for (const auto &member: group) {
        if (!member.empty()) {
            groupSize += 1;

            for (auto question: member) {
                affirmed.push_back(question);
                affirmedWithoutDoublicates.insert(question);
            }
        }
    }
}

unsigned long Decleration::affirmedQuestions() {
    return affirmedWithoutDoublicates.size();
}

int Decleration::collectivelyAffirmedQuestions() {
    int collectivelyAffirmed = 0;
    for (auto question: affirmedWithoutDoublicates) {
        int affirmationCount = 0;
        for (auto answer: affirmed) {
            affirmationCount += question == answer;
        }

        collectivelyAffirmed += affirmationCount == groupSize;
    }

    return collectivelyAffirmed;
}


vector<Decleration> createDeclerations(const vector<string> &input) {
    vector<Decleration> declerations;

    vector<string> current;
    for (const auto &line: input) {
        current.push_back(line);
        if (line.empty()) {
            declerations.emplace_back(current);
            current.clear();
        }
    }
    declerations.emplace_back(current);

    return declerations;
}

int first(const vector<string> &input) {
    vector<Decleration> declerations = createDeclerations(input);
    unsigned long affirmationCount = 0;

    for (auto decleration: declerations) {
        affirmationCount += decleration.affirmedQuestions();
    }

    cout << affirmationCount;
    return 0;
}

int second(const vector<string> &input) {
    vector<Decleration> declerations = createDeclerations(input);
    unsigned long affirmationCount = 0;

    for (auto decleration: declerations) {
        affirmationCount += decleration.collectivelyAffirmedQuestions();
    }

    cout << affirmationCount;
    return 0;
}

int main() {
    const vector<string> input = read("Input/Day_06");

    first(input);
    cout << endl;
    second(input);

    return 0;
}
