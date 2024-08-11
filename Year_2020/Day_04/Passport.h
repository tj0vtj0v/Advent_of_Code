//
// Created by Tjorven on 11.08.2024.
//

#ifndef YEAR_2020_PASSPORT_H
#define YEAR_2020_PASSPORT_H


class Passport {
public:
    explicit Passport(const vector<string> &lines);

    bool isValidAccordingToRuleOne();

    bool isValidAccordingToRuleTwo();

private:
    unordered_map<string, string> fields;
};


#endif //YEAR_2020_PASSPORT_H
