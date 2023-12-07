#!/usr/bin/env python3

import sys

from core import get_value, get_strength


def load_input(filename):
    for line in open(filename, 'r'):
        hand, bid = line.strip().split()
        yield get_value(hand), get_strength(hand), hand, int(bid)


def main():
    filename = sys.argv[1]
    hands = sorted(load_input(filename))
    acc = 0
    for rank, (value, _strength, _hand, bid) in enumerate(hands, start=1):
        # print(_hand, value, rank, bid)
        acc += rank * bid
    print(f"Solution part one: {acc}")


if __name__ == "__main__":
    main()
