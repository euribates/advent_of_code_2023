#!/usr/bin/env python3

import sys


def load_input(filename):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    for line in open(filename, 'r'):
        card, numbers = line.split(': ')
        winners_numbers, owned_numbers = numbers.split(' | ')
        yield (
            [int(_) for _ in winners_numbers.split()],
            [int(_) for _ in owned_numbers.split()],
            )


def main():
    filename = sys.argv[1]
    acc = 0
    for winners_numbers, owned_numbers in load_input(filename):
        matches = len(set(winners_numbers) & set(owned_numbers))
        acc += pow(2, matches - 1) if matches > 0 else 0
    print(f'Sol. part one: {acc}')


if __name__ == "__main__":
    main()
