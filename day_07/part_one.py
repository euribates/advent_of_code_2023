#!/usr/bin/env python3

import sys

from core import get_value, get_strength


def load_input(filename):
    with open(filename, 'r') as lines:
        for line in lines:
            hand, bid = line.strip().split()
            yield hand, int(bid)


def main():
    filename = sys.argv[1]
    hands = []
    for hand, bid in load_input(filename):
        value = get_value(hand)
        strength = get_strength(hand)
        hands.append((value, strength, hand, bid))
    hands.sort()
    acc = 0
    for rank, (value, _strength, _hand, bid) in enumerate(hands, start=1):
        # print(_hand, value, rank, bid)
        acc += rank * bid
    print(f"Solution part one: {acc}")


if __name__ == "__main__":
    main()
