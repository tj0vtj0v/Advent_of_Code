//
// Created by Tjorven on 11.08.2024.
//

#include "Decleration.h"

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
