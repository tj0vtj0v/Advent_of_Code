//
// Created by Tjorven on 12.08.2024.
//

#ifndef YEAR_2020_BUFFER_H
#define YEAR_2020_BUFFER_H


#include <numeric>
#include <algorithm>

using namespace std;

class Buffer {
public:
    Buffer(int capacity);

    int size();

    long sum();

    long min();

    long max();

    int insertNumber(long number);

    bool dualCombination(long number);

private:
    vector<long> buffer{};
    int head;
};

#include "Buffer.cpp"

#endif //YEAR_2020_BUFFER_H
