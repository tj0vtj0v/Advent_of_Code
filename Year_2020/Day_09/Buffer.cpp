//
// Created by Tjorven on 12.08.2024.
//

#include "Buffer.h"

Buffer::Buffer(int capacity) {
    for (int i = 0; i < capacity; ++i) {
        buffer.push_back(0);
    }
    head = 0;
}

int Buffer::size() {
    return buffer.size();
}

long Buffer::sum() {
    return accumulate(buffer.begin(), buffer.end(), 0);
}

long Buffer::min() {
    return min_element(buffer.begin(), buffer.end())[0];
}

long Buffer::max() {
    return max_element(buffer.begin(), buffer.end())[0];
}

int Buffer::insertNumber(long number) {
    buffer.at(head) = number;
    head = (head + 1) % size();

    return 0;
}

bool Buffer::dualCombination(long number) {
    for (int first = 0; first < size(); ++first) {
        for (int second = 0; second < size(); ++second) {
            if (buffer[first] + buffer[second] == number && first != second) {
                return true;
            }
        }
    }

    return false;
}
