//
// Created by Tjorven on 11.08.2024.
//

#include "Passport.h"

Passport::Passport(const vector<string> &lines) {
    for (const string &line: lines) {
        string rest = line;
        string current;

        while (!rest.empty()) {
            if (rest.find_last_of(' ') < rest.size()) {
                current = rest.substr(rest.find_last_of(' ') + 1, rest.size());
                rest = rest.substr(0, rest.find_last_of(' '));
            } else {
                current = rest;
                rest = "";
            }

            string field = current.substr(0, current.find(':'));
            fields[field] = current.substr(current.find(':') + 1);
        }
    }
}

bool Passport::isValidAccordingToRuleOne() {
    return fields.size() == 8 || (fields.size() == 7 && !fields.count("cid"));
}

bool Passport::isValidAccordingToRuleTwo() {
    if (!isValidAccordingToRuleOne()) {
        return false;
    }

    bool valid = stoi(fields["byr"]) >= 1920 && stoi(fields["byr"]) <= 2002;
    valid = valid && stoi(fields["iyr"]) >= 2010 && stoi(fields["iyr"]) <= 2020;
    valid = valid && stoi(fields["eyr"]) >= 2020 && stoi(fields["eyr"]) <= 2030;

    if (fields["hgt"].find("cm") < fields["hgt"].size()) {
        const int height = stoi(fields["hgt"].substr(0, fields["hgt"].size() - 2));
        valid = valid && height >= 150 && height <= 193;
    } else if (fields["hgt"].find("in") < fields["hgt"].size()) {
        const int height = stoi(fields["hgt"].substr(0, fields["hgt"].size() - 2));
        valid = valid && height >= 59 && height <= 76;
    } else {
        return false;
    }

    const string hairColor = fields["hcl"].substr(1, fields["hcl"].size());
    if (fields["hcl"].find('#') != 0) {
        if (hairColor.find_first_not_of("0123456789abcdef") < hairColor.size() || hairColor.size() != 6) {
            return false;
        }
    }

    bool validEyeColor = false;
    vector<string> eyeColors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
    for (const auto &eyeColor: eyeColors) {
        if (fields["ecl"] == eyeColor) {
            validEyeColor = true;
            break;
        }
    }
    valid = valid && validEyeColor;

    if (fields["pid"].find_first_not_of("0123456789") < fields["pid"].size() || fields["pid"].size() != 9) {
        return false;
    }

    return valid;
}
