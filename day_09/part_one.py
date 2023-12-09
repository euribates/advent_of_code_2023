#!/usr/bin/env python3

from itertools import tee
import sys


def batched(sequence):
    first, second = tee(sequence)
    next(second)
    for a, b in zip(first, second):
        yield a, b


def load_input(filename):
    with open(filename) as file_input:
        for line in file_input:
            line = line.strip()
            yield [int(n) for n in line.split()]

def predict_next(numbers):
    delta = numbers[-1]
    accs = [(b - a) for a, b in batched(numbers)]
    while any(accs):
        delta += accs[-1]
        numbers = accs
        accs = [(b - a) for a, b in batched(numbers)]
    return delta


def main():
    filename = sys.argv[1]
    acc = 0
    for numbers in load_input(filename):
        # print(numbers, predict_next(numbers))
        acc += predict_next(numbers)
    print(f"Solution part one: {acc}")


if __name__ == '__main__':
    main()
