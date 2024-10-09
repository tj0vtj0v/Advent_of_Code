//
// Created by Tjorven on 19.08.2024.
//

#ifndef YEAR_2020_MATHQUEUE_H
#define YEAR_2020_MATHQUEUE_H


#include <iostream>
#include <queue>

using namespace std;

class MathQueue {
public:
    MathQueue();

    MathQueue(const string &expression);

    bool empty();

    char dequeue();

    int enqueue(const char &symbol);

    int evaluate();

private:
    queue<char> symbols;
};

#include "MathQueue.cpp"

#endif //YEAR_2020_MATHQUEUE_H
