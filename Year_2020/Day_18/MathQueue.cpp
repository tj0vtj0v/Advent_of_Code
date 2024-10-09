//
// Created by Tjorven on 19.08.2024.
//

#include "MathQueue.h"

MathQueue::MathQueue() : MathQueue(""){
}

MathQueue::MathQueue(const string &expression) {
    enqueue('+');
    for (auto symbol: expression) {
        if (symbol != ' ') {
            enqueue(symbol);
        }
    }
}

bool MathQueue::empty() {
    return symbols.empty();
}

char MathQueue::dequeue() {
    if (!symbols.empty()) {
        char temp = symbols.front();
        symbols.pop();

        return temp;
    }
}

int MathQueue::enqueue(const char &symbol) {
    symbols.push(symbol);

    return 0;
}

int MathQueue::evaluate() {
    int result = 0;
    char operation;
    char next;
    int value;

    while (!empty()) {
        operation = dequeue();
        next = dequeue();

        if (!isdigit(next)) {
            int open = 1;
            auto helper = MathQueue();

            while (true) {
                next = dequeue();

                if (next == '(') {
                    open++;
                }
                if (next == ')') {
                    open--;
                }

                if (open > 0) {
                    helper.enqueue(next);
                } else {
                    break;
                }
            }

            value = helper.evaluate();
        } else {
            value = next - '0';
        }

        if (operation == '+') {
            result += value;
        } else {
            result *= value;
        }
    }

    return result;
}
