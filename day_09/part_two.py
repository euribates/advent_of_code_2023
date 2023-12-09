#!/usr/bin/env python3

from itertools import tee
from functools import reduce

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


def predict_prev(numbers):
    deltas = [numbers[0]]
    accs = [(b - a) for a, b in batched(numbers)]
    while any(accs):
        numbers = accs
        deltas.append(numbers[0])
        accs = [(b - a) for a, b in batched(numbers)]
    deltas.append(0)
    deltas.reverse()
    # print(f'deltas: {deltas}', end=' ')
    result = reduce(lambda a, b: b - a, deltas, 0)
    # print(result)
    return result

def main():
    filename = sys.argv[1]
    acc = 0
    for numbers in load_input(filename):
        # print(numbers, predict_prev(numbers))
        acc += predict_prev(numbers)
    print(f"Solution part two: {acc}")


if __name__ == '__main__':
    main()
